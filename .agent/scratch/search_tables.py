import asyncio
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def main():
    token_provider = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(token_provider)
    db = SankhyaDbExplorerRepository(gateway)
    
    # Pesquisa tabelas com nome similar
    sql = "SELECT name FROM sys.tables WHERE name LIKE '%SINAL%SHEET%'"
    res = await db.execute_query(sql)
    rows = db.to_rows(res)
    print("--- TABELAS ENCONTRADAS ---")
    for r in rows:
        print(f"Table: {r['name']}")

if __name__ == "__main__":
    asyncio.run(main())
