import json
import os
import sys

# Adiciona o diretório raiz ao path para importar o serviço
sys.path.append(os.getcwd())

from app.services.vibra_routing import VibraRoutingService

def main():
    sync_path = "app/data/vibra/latest_sync.json"
    if not os.path.exists(sync_path):
        print(f"Erro: {sync_path} não encontrado.")
        return

    with open(sync_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    router = VibraRoutingService()
    
    print("Iniciando cálculo de logística para orçamentos...")
    
    # Processa Budgets
    for b in data.get("budgets", []):
        address = b.get("endereco")
        if address and address != "N/A":
            print(f"Calculando distância para: {b.get('FuelStationName')}...")
            distance = router.calcular_distancia_orcamento(
                address, 
                b.get("cidade", ""), 
                b.get("uf", "")
            )
            if distance:
                b["distancia_km"] = round(distance, 2)
                print(f"  -> {b['distancia_km']} KM")
            else:
                print(f"  -> Falha ao calcular distância para {address}")

    # Processa Monitoring (Obras)
    for m in data.get("monitoring", []):
        address = m.get("endereco")
        if address and address != "N/A":
            print(f"Calculando distância para Obra: {m.get('cliente')}...")
            distance = router.calcular_distancia_orcamento(
                address,
                m.get("cidade", ""),
                m.get("uf", "")
            )
            if distance:
                m["distancia_km"] = round(distance, 2)
                print(f"  -> {m['distancia_km']} KM")
            else:
                print(f"  -> Falha ao calcular distância para {address}")

    with open(sync_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("\nLogística atualizada no latest_sync.json com sucesso!")

if __name__ == "__main__":
    main()
