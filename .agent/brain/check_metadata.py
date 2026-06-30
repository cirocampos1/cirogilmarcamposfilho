import asyncio
import os
import sys
import json

# Add path to load our modules
sys.path.append('/home/leonardobarbosa/dev/')

from app.dependencies.sankhya import get_db_repository

async def main():
    repo = get_db_repository()
    
    queries = {
        "Physical Table": "SELECT name FROM sys.tables WHERE name = 'AD_SINAL_SHEET'",
        "Metadata TDDTAB": "SELECT * FROM sankhya.TDDTAB WHERE NOMETAB = 'AD_SINAL_SHEET'",
        "Metadata TDDCAM (count)": "SELECT COUNT(*) as QTY FROM sankhya.TDDCAM WHERE NOMETAB = 'AD_SINAL_SHEET'",
        "Metadata TDDINS": "SELECT * FROM sankhya.TDDINS WHERE NOMETAB = 'AD_SINAL_SHEET'"
    }
    
    results = {}
    for label, sql in queries.items():
        try:
            res = await repo.execute_query(sql)
            rows = repo.to_rows(res)
            results[label] = rows
        except Exception as e:
            results[label] = str(e)
            
    print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(main())
