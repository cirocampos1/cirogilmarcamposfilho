import asyncio
import json
from app.repositories.vibra_sankhya_repository import VibraSankhyaRepository
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider

async def main():
    token_provider = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(token_provider)
    db_explorer = SankhyaDbExplorerRepository(gateway)
    repo = VibraSankhyaRepository(db_explorer)
    
    print("--- Verificando Obras no Sankhya ---")
    obras = await repo.get_obras()
    if not obras:
        print("Nenhuma obra encontrada no banco.")
        return
        
    print(f"Total de obras no banco: {len(obras)}")
    for i, obra in enumerate(obras[:3]):
        json_raw = obra.get("JSON_FULL") or "{}"
        try:
            data = json.loads(json_raw)
            has_bom = "bom" in data and len(data.get("bom", [])) > 0
            print(f"Obra {obra.get('ID_PORTAL')}: {obra.get('CLIENTE')} | BOM presente: {has_bom}")
            if has_bom:
                print(f"  Exemplo BOM: {data['bom'][0]}")
        except:
            print(f"Obra {obra.get('ID_PORTAL')}: Erro ao decodificar JSON")

if __name__ == "__main__":
    asyncio.run(main())
