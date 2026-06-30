import asyncio
import sys
sys.path.append("/home/leonardobarbosa/dev/")
from app.dependencies.sankhya import get_db_repository

async def main():
    db = get_db_repository()
    sql = "SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('dbo.AD_SH_QUAL_ANC')"
    try:
        res = await db.execute_query(sql)
        rows = db.to_rows(res)
        if not rows:
            print("No columns found (table might not exist or schema is different).")
            return
        print(f"Columns found ({len(rows)}):")
        for row in rows:
            # Print keys and values to be sure
            print(row)
    except Exception as e:
        print("Error checking columns:", e)

if __name__ == "__main__":
    asyncio.run(main())
