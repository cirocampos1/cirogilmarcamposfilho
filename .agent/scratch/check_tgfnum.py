import asyncio
import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider

async def main():
    tp = SankhyaTokenProvider()
    g = SankhyaGatewayClient(tp)
    r = SankhyaDbExplorerRepository(g)
    try:
        res = await r.execute_query("SELECT ULTIMO FROM TGFNUM WHERE ARQUIVO = 'TGFCAB'")
        print(f"RESULT:{res}")
    except Exception as e:
        print(f"ERROR:{e}")

if __name__ == "__main__":
    asyncio.run(main())
