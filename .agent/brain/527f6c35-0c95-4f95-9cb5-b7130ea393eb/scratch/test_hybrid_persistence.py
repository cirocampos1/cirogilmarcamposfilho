import asyncio
import os
import sys
from datetime import date
import logging

# Configuração de Logs para ver o diagnóstico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(".test")

sys.path.append(os.getcwd())

from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository
from app.repositories.sinalsheet_repository import SinalSheetRepository

async def test_hybrid():
    tp = SankhyaTokenProvider()
    gw = SankhyaGatewayClient(tp)
    db = SankhyaDbExplorerRepository(gw)
    repo = SinalSheetRepository(db, gw)
    
    username = "leonardo.barbosa"
    
    print("\n--- INICIANDO TESTE DE PERSISTÊNCIA HÍBRIDA ---")
    try:
        res = await repo.create_lancamento(
            username=username,
            display_name="Teste Hibrido Antigravity",
            dt_lancamento=date.today(),
            codproj=0,
            nome_projeto="PROJETO TESTE",
            motivo="TESTE SISTEMA",
            horas=0.5,
            complexidade="Baixa",
            observacao="Teste de diagnóstico de entidade"
        )
        print("\n✅ SUCESSO! Registro criado.")
        print(f"Dados retornados: {res}")
        
        # Limpeza (opcional)
        if "ID" in res:
            print(f"\nRemovendo registro de teste ID {res['ID']}...")
            await repo.delete_lancamento(res["ID"], username)
            print("✅ Registro removido.")
            
    except Exception as e:
        print(f"\n❌ FALHA: {e}")
    finally:
        await gw.aclose()

if __name__ == "__main__":
    asyncio.run(test_hybrid())
