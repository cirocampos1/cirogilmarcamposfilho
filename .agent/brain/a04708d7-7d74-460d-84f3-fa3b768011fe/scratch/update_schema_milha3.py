import asyncio
import logging
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("schema_update")

async def update_schema():
    try:
        tp = SankhyaTokenProvider()
        gw = SankhyaGatewayClient(tp)
        db = SankhyaDbExplorerRepository(gw)
        
        # 1. Adicionar coluna DT_INI_FAB
        logger.info("🛠️ Passo 1: Adicionando coluna DT_INI_FAB...")
        sql_col = "ALTER TABLE sankhya.AD_VIBRA_OBRAS ADD DT_INI_FAB DATE"
        try:
            await db.execute_query(sql_col)
            logger.info("✅ Coluna DT_INI_FAB adicionada.")
        except Exception as e:
            if "already exists" in str(e).lower() or "já existe" in str(e).lower():
                logger.info("ℹ️ Coluna DT_INI_FAB já existe.")
            else:
                logger.error(f"❌ Erro ao adicionar coluna: {e}")

        # 2. Atualizar Stored Procedure
        logger.info("🛠️ Passo 2: Atualizando Stored Procedure AD_STP_VIBRA_SYNC...")
        
        # Como o gateway pode não gostar de CREATE OR ALTER em um comando genérico, 
        # vamos tentar apenas o corpo da procedure se possível, ou garantir que seja o único comando.
        
        sql_sp = """
CREATE OR ALTER PROCEDURE sankhya.AD_STP_VIBRA_SYNC
    @P_ID_PORTAL DECIMAL(18,0),
    @P_CLIENTE VARCHAR(255),
    @P_UF VARCHAR(2),
    @P_CIDADE VARCHAR(100),
    @P_FRENTE VARCHAR(255),
    @P_STATUS VARCHAR(100),
    @P_INICIO VARCHAR(20),
    @P_FIM VARCHAR(20),
    @P_VALOR DECIMAL(15,2),
    @P_JSON NVARCHAR(MAX),
    @P_DT_INI_FAB DATE = NULL
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    DECLARE @V_OLD_STATUS VARCHAR(100);
    DECLARE @V_OLD_FIM VARCHAR(20);

    BEGIN TRY
        BEGIN TRANSACTION;

        SELECT @V_OLD_STATUS = STATUS_VIBRA, @V_OLD_FIM = FIM_OBRA
        FROM sankhya.AD_VIBRA_OBRAS
        WHERE ID_PORTAL = @P_ID_PORTAL;

        IF @V_OLD_STATUS IS NOT NULL OR @V_OLD_FIM IS NOT NULL
        BEGIN
            IF ISNULL(@V_OLD_STATUS, '') <> ISNULL(@P_STATUS, '')
                INSERT INTO sankhya.AD_VIBRA_HIST (ID_PORTAL, CAMPO, VALOR_ANT, VALOR_NOVO)
                VALUES (@P_ID_PORTAL, 'STATUS_VIBRA', @V_OLD_STATUS, @P_STATUS);

            IF ISNULL(@V_OLD_FIM, '') <> ISNULL(@P_FIM, '')
                INSERT INTO sankhya.AD_VIBRA_HIST (ID_PORTAL, CAMPO, VALOR_ANT, VALOR_NOVO)
                VALUES (@P_ID_PORTAL, 'FIM_OBRA', @V_OLD_FIM, @P_FIM);
        END;

        IF EXISTS (SELECT 1 FROM sankhya.AD_VIBRA_OBRAS WHERE ID_PORTAL = @P_ID_PORTAL)
        BEGIN
            UPDATE sankhya.AD_VIBRA_OBRAS
            SET
                CLIENTE = @P_CLIENTE,
                UF = @P_UF,
                CIDADE = @P_CIDADE,
                FRENTE = @P_FRENTE,
                STATUS_VIBRA = @P_STATUS,
                INICIO_OBRA = @P_INICIO,
                FIM_OBRA = @P_FIM,
                VALOR_EST = @P_VALOR,
                DT_ULT_SYNC = SYSDATETIME(),
                JSON_FULL = @P_JSON,
                DT_INI_FAB = ISNULL(@P_DT_INI_FAB, DT_INI_FAB)
            WHERE ID_PORTAL = @P_ID_PORTAL;
        END
        ELSE
        BEGIN
            INSERT INTO sankhya.AD_VIBRA_OBRAS (
                ID_PORTAL, CLIENTE, UF, CIDADE, FRENTE, STATUS_VIBRA, 
                INICIO_OBRA, FIM_OBRA, VALOR_EST, JSON_FULL, DT_INI_FAB
            )
            VALUES (
                @P_ID_PORTAL, @P_CLIENTE, @P_UF, @P_CIDADE, @P_FRENTE, @P_STATUS, 
                @P_INICIO, @P_FIM, @P_VALOR, @P_JSON, @P_DT_INI_FAB
            );
        END;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
        """
        await db.execute_query(sql_sp)
        logger.info("✅ Stored Procedure atualizada.")
        
    except Exception as e:
        logger.error(f"❌ Erro: {e}")

if __name__ == "__main__":
    asyncio.run(update_schema())
