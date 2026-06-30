import asyncio
import json
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def inspect_json():
    db = SankhyaDbExplorerRepository(SankhyaGatewayClient(SankhyaTokenProvider()))
    # Pega o JSON da obra 4836
    sql = "SELECT ID_PORTAL, DT_ULT_SYNC, JSON_FULL FROM sankhya.AD_VIBRA_OBRAS WHERE ID_PORTAL = 4836"
    resp = await db.execute_query(sql)
    rows = db.to_rows(resp)
    if rows:
        row = rows[0]
        print(f"ID: {row['ID_PORTAL']}")
        print(f"ULT_SYNC: {row['DT_ULT_SYNC']}")
        # Tenta parsear o JSON para ver se tem dados novos
        try:
            js = json.loads(row['JSON_FULL'])
            print("JSON Status Obra:", js.get('status_obra'))
            print("JSON Status Montagem:", js.get('status_montagem'))
        except:
            print("JSON_FULL está corrompido ou não é um JSON válido.")
    else:
        print("Obra 4836 não encontrada.")

if __name__ == "__main__":
    asyncio.run(inspect_json())
