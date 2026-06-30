import asyncio
import os
import sys

# Add the project root to sys.path
sys.path.append(os.getcwd())

from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def check():
    tp = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(tp)
    repo = SankhyaDbExplorerRepository(gateway)
    # Changed alias TOP to TP to avoid SQL Server keyword conflict
    sql = "SELECT CAB.CODTIPOPER, TP.DESCROPER FROM TGFCAB CAB INNER JOIN TGFTOP TP ON TP.CODTIPOPER = CAB.CODTIPOPER AND TP.DHALTER = CAB.DHTIPOPER WHERE NUNOTA = 2858577"
    r = await repo.execute_query(sql)
    print(repo.to_rows(r))

if __name__ == "__main__":
    asyncio.run(check())
