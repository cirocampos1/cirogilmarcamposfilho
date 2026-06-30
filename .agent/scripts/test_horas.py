import asyncio
import os
import sys

# Ensure imports work from the root of the project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from app.core.config import settings
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.dependencies.sankhya import get_sankhya_gateway

async def test_sankhya():
    gateway = await get_sankhya_gateway()
    
    action_id = "245" # Assuming 245 from your .env
    
    # Try different combinations
    horas_to_test = [1.5, "1.5", "1,5", 2, "2"]
    
    for hora in horas_to_test:
        print(f"\n--- Testando HORAS={hora} (tipo {type(hora)}) ---")
        
        # Determine Sankhya API Type
        p_type = "S"
        if isinstance(hora, (int, float)):
            p_type = "I" if isinstance(hora, int) else "D"
            
        param_list = [
            {"type": "I", "paramName": "CODEMP", "$": "1"},
            {"type": "S", "paramName": "ACAO", "$": "SINALSHEET_SAVE"},
            {"type": "S", "paramName": "USERNAME", "$": "teste"},
            {"type": "S", "paramName": "DT_LANCAMENTO", "$": "2024-10-10"},
            {"type": "S", "paramName": "NOME_PROJETO", "$": "Teste"},
            {"type": "S", "paramName": "MOTIVO", "$": "PROJETO"},
            {"type": p_type, "paramName": "HORAS", "$": str(hora)},
            {"type": "S", "paramName": "COMPLEXIDADE", "$": "M"},
            {"type": "S", "paramName": "REQ_ID", "$": f"TEST-{str(hora).replace('.','_').replace(',','_')}"},
        ]
        
        payload = {
            "clientEventList": {
                "clientEvent": [{"$": "Action"}]
            },
            "javaCall": {
                "actionID": action_id,
                "refreshType": "ALL",
                "params": {"param": param_list},
                "rows": {"row": [{"field": [{"fieldName": "NUNOTA", "$": "0"}]}]},
            },
        }

        try:
            resp = await gateway.call("ActionButtonsSP.executeJava", payload)
            print("SUCESSO:", resp)
        except Exception as e:
            print("ERRO:", str(e))

if __name__ == "__main__":
    asyncio.run(test_sankhya())
