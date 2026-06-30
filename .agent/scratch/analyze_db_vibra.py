import asyncio
import os
import sys
import json

# Add current directory to path
sys.path.append(os.getcwd())

from app.routers.vibra import _get_vibra_repo

async def main():
    repo = _get_vibra_repo()
    obras_db = await repo.get_obras()
    
    total = len(obras_db)
    monitoring = 0
    budgets = 0
    both = 0
    neither = 0
    
    for row in obras_db:
        json_raw = row.get("JSON_FULL") or row.get("json_full") or "{}"
        try:
            obra_json = json.loads(json_raw)
        except:
            neither += 1
            continue
            
        has_monitoring = "status_obra" in obra_json or "CurrentStartDate" in json_raw
        has_bom = "bom" in obra_json and len(obra_json.get("bom", [])) > 0
        
        if has_monitoring and has_bom:
            both += 1
        elif has_monitoring:
            monitoring += 1
        elif has_bom:
            budgets += 1
        else:
            neither += 1
            
    print(f"Total: {total}")
    print(f"Só Monitoramento: {monitoring}")
    print(f"Só Orçamentos (BOM): {budgets}")
    print(f"Ambos: {both}")
    print(f"Nenhum: {neither}")

if __name__ == "__main__":
    asyncio.run(main())
