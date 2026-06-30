import asyncio
import sys
sys.path.append("/home/leonardobarbosa/dev/")
from app.dependencies.sankhya import get_db_repository

async def main():
    db = get_db_repository()
    sql = """
    IF NOT EXISTS (SELECT * FROM sys.columns WHERE object_id = OBJECT_ID(N'[AD_SH_QUAL_ANC]') AND name = 'PRODUTO_NOME')
        ALTER TABLE [AD_SH_QUAL_ANC] ADD [PRODUTO_NOME] VARCHAR(255) NULL;
    IF NOT EXISTS (SELECT * FROM sys.columns WHERE object_id = OBJECT_ID(N'[AD_SH_QUAL_ANC]') AND name = 'ANEXOS')
        ALTER TABLE [AD_SH_QUAL_ANC] ADD [ANEXOS] VARCHAR(MAX) NULL;
    """
    try:
        res = await db.execute_query(sql)
        print("Success:", res)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())
