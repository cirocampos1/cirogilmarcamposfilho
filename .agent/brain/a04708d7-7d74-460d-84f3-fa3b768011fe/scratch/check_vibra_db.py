import asyncio
import json
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository
from app.repositories.vibra_sankhya_repository import VibraSankhyaRepository

async def check():
    try:
        tp = SankhyaTokenProvider()
        gw = SankhyaGatewayClient(tp)
        db = SankhyaDbExplorerRepository(gw)
        repo = VibraSankhyaRepository(db)
        
        print("🔍 Buscando obras no Sankhya...")
        obras = await repo.get_obras()
        
        print(f"✅ Total de obras encontradas: {len(obras)}")
        
        if obras:
            print("\n📋 Amostra da primeira obra:")
            # Remove o JSON_FULL gigante para não poluir o log, mas mostra as chaves
            amostra = obras[0].copy()
            json_str = amostra.get("JSON_FULL", "{}")
            try:
                js = json.loads(json_str)
                print(f"   Chaves no JSON_FULL: {list(js.keys())}")
                print(f"   Status no JSON: {js.get('Status') or js.get('status')}")
                print(f"   Progresso no JSON: {js.get('progress_overall')}")
            except:
                print("   [!] Erro ao parsear JSON_FULL")
            
            # Mostra dados das colunas
            del amostra["JSON_FULL"]
            print(json.dumps(amostra, indent=2))
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    asyncio.run(check())
