import asyncio
import logging
from unittest.mock import MagicMock, AsyncMock

from app.services.oracle.snapshot import OracleSnapshotService

# Configurar logging
logging.basicConfig(level=logging.INFO)

async def test_snapshot():
    # Mock services
    fat_service = MagicMock()
    fat_service.fetch_dashboard_data = AsyncMock(return_value={"success": True, "kpis": {"faturamento_realizado": 1000, "faturamento_pendente": 500, "total_notas": 10}})
    
    saida_dia_service = MagicMock()
    saida_dia_service.repository.get_saida_dia_data = AsyncMock(return_value=[{"AD_STATUSFATURAMENTO": "FR"}, {"AD_STATUSFATURAMENTO": "PE", "is_atrasado": True}])
    
    kanban_service = MagicMock()
    kpis_mock = MagicMock()
    kpis_mock.score_saude = 85
    kpis_mock.cor_score = "green"
    kpis_mock.produtos_criticos = 2
    kpis_mock.taxa_ruptura = 0.05
    kpis_mock.valor_em_estoque = 500000
    kanban_service.get_kpis = AsyncMock(return_value=kpis_mock)
    
    service = OracleSnapshotService(
        faturamento_service=fat_service,
        saida_dia_service=saida_dia_service,
        kanban_service=kanban_service
    )
    
    print("Testando get_factory_snapshot...")
    result = await service.get_factory_snapshot(codemp=1)
    import json
    print(json.dumps(result, indent=2))
    
    assert result["success"] is True
    assert "snapshot" in result
    assert result["snapshot"]["faturamento_hoje"]["realizado"] == 1000
    assert result["snapshot"]["logistica_saida"]["total_pvs_planejados"] == 2
    print("Teste concluído com sucesso!")

if __name__ == "__main__":
    asyncio.run(test_snapshot())
