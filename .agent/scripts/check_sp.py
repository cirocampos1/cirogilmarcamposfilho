import asyncio
import sys
from uuid import uuid4
sys.path.append("/home/leonardobarbosa/dev/")

from app.dependencies.sankhya import get_db_repository

async def test_procedure():
    db = get_db_repository()
    req_id = f"SSH-{uuid4().hex[:12].upper()}"
    
    params = {
        "ID": None,
        "USERNAME": "pedromenezes",
        "DISPLAY_NAME": "Pedro Menezes",
        "DT_LANCAMENTO": "2024-10-10",
        "CODPROJ": None,
        "NOME_PROJETO": "Test SP",
        "MOTIVO": "PROJETO",
        "HORAS": 2,
        "COMPLEXIDADE": "M",
        "OBSERVACAO": "",
        "REQ_ID": req_id
    }
    
    try:
        resp = await db.execute_stored_procedure("sankhya.AD_STP_SAVE_SINAL_SHEET", params)
        print("RESULTADO:", resp)
        
        # Check DB to see if it inserted
        check_sql = f"SELECT ID FROM sankhya.AD_SINAL_SHEET WHERE REQ_ID = '{req_id}'"
        res = await db.execute_query(check_sql)
        print("FOI INSERIDO?", db.to_rows(res))
    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    asyncio.run(test_procedure())
