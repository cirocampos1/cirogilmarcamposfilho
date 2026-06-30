import asyncio
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def main():
    token_provider = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(token_provider)
    db = SankhyaDbExplorerRepository(gateway)
    
    # Pega uma linha completa para ver os valores e nomes de campos
    sql = "SELECT TOP 1 * FROM sankhya.AD_SINAL_SHEET"
    res = await db.execute_query(sql)
    rows = db.to_rows(res)
    print("--- DADO AD_SINAL_SHEET ---")
    if rows:
        for k, v in rows[0].items():
            print(f"{k}: {v}")
    else:
        print("Tabela vazia.")

if __name__ == "__main__":
    asyncio.run(main())
