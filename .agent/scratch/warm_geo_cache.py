import json
from app.services.vibra_routing import routing_service

def warm_cache():
    sync_path = "app/data/vibra/latest_sync.json"
    with open(sync_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print("Iniciando pré-aquecimento de cache de logística...")
    
    items = data.get("monitoring", []) + data.get("budgets", [])
    unique_locations = {}
    
    for item in items:
        addr = item.get("endereco")
        cid = item.get("cidade")
        uf = item.get("uf", "MG")
        if addr and cid:
            key = f"{addr}, {cid}, {uf}"
            unique_locations[key] = (addr, cid, uf)
    
    print(f"Encontradas {len(unique_locations)} localizações únicas para geocodificar.")
    
    for key, (addr, cid, uf) in unique_locations.items():
        print(f"Geocodificando: {cid}-{uf}...")
        routing_service.calcular_distancia_orcamento(addr, cid, uf)
    
    print("Cache aquecido com sucesso!")

if __name__ == "__main__":
    warm_cache()
