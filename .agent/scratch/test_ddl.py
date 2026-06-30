import asyncio
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def main():
    token_provider = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(token_provider)
    db = SankhyaDbExplorerRepository(gateway)
    
    print("--- TESTE PERMISSÃO DDL ---")
    # Tenta criar uma tabela temporária de teste
    sql = "CREATE TABLE sankhya.AD_TEST_DDL_ANTIGRAVITY (ID INT)"
    try:
        res = await db.execute_query(sql)
        print("PERMISSÃO DDL CONFIRMADA (Tabela criada)")
        # Deleta se funcionou
        await db.execute_query("DROP TABLE sankhya.AD_TEST_DDL_ANTIGRAVITY")
    except Exception as e:
        print(f"SEM PERMISSÃO DDL: {e}")

if __name__ == "__main__":
    asyncio.run(main())
