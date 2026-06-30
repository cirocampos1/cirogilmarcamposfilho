import asyncio
import logging
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def fix_schema():
    logging.basicConfig(level=logging.INFO)
    db = SankhyaDbExplorerRepository(SankhyaGatewayClient(SankhyaTokenProvider()))
    
    print("Checking columns...")
    # Tenta ler as colunas
    cols_to_add = [
        ("STATUS_MONT", "VARCHAR(100)"),
        ("SLA", "INT"),
        ("SLA_REST", "INT"),
        ("DT_INI_TRANS", "DATE"),
        ("DT_FIM_TRANS", "DATE"),
        ("DT_INI_MONT", "DATE"),
        ("DT_FIM_MONT", "DATE")
    ]
    
    for col, type_ in cols_to_add:
        try:
            print(f"Adding column {col}...")
            await db.execute_query(f"ALTER TABLE sankhya.AD_VIBRA_OBRAS ADD {col} {type_}")
            print(f"✅ Column {col} added.")
        except Exception as e:
            if "already exists" in str(e).lower() or "já existe" in str(e).lower():
                print(f"ℹ️ Column {col} already exists.")
            else:
                print(f"❌ Error adding {col}: {e}")

if __name__ == "__main__":
    asyncio.run(fix_schema())
