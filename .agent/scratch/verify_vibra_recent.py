import asyncio
import json
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def verify_recent():
    db = SankhyaDbExplorerRepository(SankhyaGatewayClient(SankhyaTokenProvider()))
    # Busca obras com IDs altos (recentes) e vê se o Sync de hoje bateu
    sql = "SELECT TOP 5 ID_PORTAL, STATUS_VIBRA, STATUS_MONT, SLA, DT_ULT_SYNC FROM sankhya.AD_VIBRA_OBRAS ORDER BY ID_PORTAL DESC"
    resp = await db.execute_query(sql)
    rows = db.to_rows(resp)
    print(json.dumps(rows, indent=2, ensure_ascii=False, default=str))

if __name__ == "__main__":
    asyncio.run(verify_recent())
