import asyncio
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def main():
    token_provider = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(token_provider)
    db = SankhyaDbExplorerRepository(gateway)
    
    # Tenta JOIN para buscar Cliente e Tipo via TCSPRJ
    sql = """
    SELECT TOP 10
        S.ID,
        S.CODPROJ,
        P.ABREVIATURA,
        ISNULL(C.NOMEPARC, 'CLI_DESCONHECIDO') as CLIENTE,
        ISNULL(P.AD_TIPODEFRETE, 'TIPO_DESCONHECIDO') as TIPO_PROJ_FALLBACK
    FROM sankhya.AD_SINAL_SHEET S
    LEFT JOIN sankhya.TCSPRJ P ON S.CODPROJ = P.CODPROJ
    LEFT JOIN sankhya.TGFPAR C ON P.CODCLT = C.CODPARC
    WHERE S.CODPROJ IS NOT NULL
    """
    try:
        res = await db.execute_query(sql)
        rows = db.to_rows(res)
        if not rows:
            print("Nenhum dado encontrado com CODPROJ.")
        for r in rows:
            print(f"ID: {r['ID']} | Proj: {r['ABREVIATURA']} | Cliente: {r['CLIENTE']} | Tipo: {r['TIPO_PROJ_FALLBACK']}")
    except Exception as e:
        print(f"ERRO: {e}")

if __name__ == "__main__":
    asyncio.run(main())
