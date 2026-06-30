import asyncio
import json
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def check_precision():
    db = SankhyaDbExplorerRepository(SankhyaGatewayClient(SankhyaTokenProvider()))
    sql = "SELECT COLUMN_NAME, DATA_TYPE, NUMERIC_PRECISION, NUMERIC_SCALE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'AD_VIBRA_OBRAS' AND COLUMN_NAME = 'ID_PORTAL'"
    resp = await db.execute_query(sql)
    print(json.dumps(db.to_rows(resp), indent=2))

if __name__ == "__main__":
    asyncio.run(check_precision())
