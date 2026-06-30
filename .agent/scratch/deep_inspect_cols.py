import asyncio
import logging
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def main():
    token_provider = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(token_provider)
    db = SankhyaDbExplorerRepository(gateway)
    
    print("--- PESQUISA TCSPRJ ---")
    sql_prj = "SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('sankhya.TCSPRJ') AND (name LIKE '%TIPO%' OR name LIKE '%CLT%')"
    res_prj = await db.execute_query(sql_prj)
    rows_prj = db.to_rows(res_prj)
    for r in rows_prj:
        print(f"TCSPRJ Col: {r['name']}")

    print("\n--- PESQUISA AD_SINAL_SHEET ---")
    sql_ss = "SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('sankhya.AD_SINAL_SHEET')"
    res_ss = await db.execute_query(sql_ss)
    rows_ss = db.to_rows(res_ss)
    for r in rows_ss:
        print(f"AD_SINAL_SHEET Col: {r['name']}")

if __name__ == "__main__":
    asyncio.run(main())
