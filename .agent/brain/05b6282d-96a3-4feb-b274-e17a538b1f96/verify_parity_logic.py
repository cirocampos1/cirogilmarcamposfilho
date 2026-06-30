import asyncio
from unittest.mock import AsyncMock, MagicMock
from app.services.faturamento_intelligence_service import FaturamentoIntelligenceService
from app.repositories.faturamento_intelligence_repository import IntelligenceParams

async def verify_logic_parity():
    # Valores extraídos das imagens de referência
    TARGET_ORDERS = 1089206657.20
    TARGET_BILLED = 1051146609.66
    
    # Mock do Repositório
    repo = MagicMock()
    # No Nível 1, o repositório retorna o faturamento bruto agregado por segmento
    repo.get_orders_by_segment = AsyncMock(return_value=[
        {"CODPROJPAI": 100000000, "SEGMENTO": "TOTAL", "TOTAL_BRUTO": TARGET_ORDERS}
    ])
    repo.get_billed_by_segment = AsyncMock(return_value=[
        {"CODPROJPAI": 100000000, "SEGMENTO": "TOTAL", "TOTAL_FATURADO": TARGET_BILLED}
    ])
    
    service = FaturamentoIntelligenceService(repo)
    params = IntelligenceParams(data_ini="2024-01-01", data_fin="2024-12-31", codemp=1)
    
    result = await service.fetch_matrix_data(params)
    
    print(f"--- Verificação de Paridade ---")
    matrix = result["matrix"]
    total_pedidos = sum(item["pedido_total"] for item in matrix)
    total_faturamento = sum(item["faturado_total"] for item in matrix)
    
    print(f"Target Pedidos: {TARGET_ORDERS:,.2f}")
    print(f"Hub Pedidos:    {total_pedidos:,.2f}")
    print(f"Status:         {'MATCH ✅' if abs(total_pedidos - TARGET_ORDERS) < 0.01 else 'DIVERGENTE ❌'}")
    
    print(f"\nTarget Faturamento: {TARGET_BILLED:,.2f}")
    print(f"Hub Faturamento:    {total_faturamento:,.2f}")
    print(f"Status:             {'MATCH ✅' if abs(total_faturamento - TARGET_BILLED) < 0.01 else 'DIVERGENTE ❌'}")

if __name__ == "__main__":
    asyncio.run(verify_logic_parity())
