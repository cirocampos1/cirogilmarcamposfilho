import asyncio
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def main():
    token_provider = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(token_provider)
    db = SankhyaDbExplorerRepository(gateway)
    
    # Lista TODAS as colunas de AD_SINAL_SHEET para ter certeza absoluta
    sql = "SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('sankhya.AD_SINAL_SHEET')"
    res = await db.execute_query(sql)
    rows = db.to_rows(res)
    print("--- COLUNAS AD_SINAL_SHEET ---")
    for r in rows:
        print(f"Col: {r['name']}")

if __name__ == "__main__":
    asyncio.run(main())
