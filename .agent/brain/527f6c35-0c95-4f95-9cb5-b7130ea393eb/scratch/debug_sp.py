import asyncio
import os
from datetime import date
from app.dependencies.sankhya import get_sinalsheet_repository
from app.clients.sankhya.gateway_client import SankhyaGatewayError

async def debug_sp():
    repo = get_sinalsheet_repository()
    
    print("Tentando criar lançamento via SP...")
    try:
        res = await repo.create_lancamento(
            username="leonardo.barbosa",
            display_name="Leonardo Barbosa",
            dt_lancamento=date.today(),
            codproj=1,
            nome_projeto="PROJETO TESTE",
            motivo="ADMINISTRATIVO",
            horas=1.0,
            complexidade="M",
            observacao="Teste de debug"
        )
        print("Sucesso!")
        print(res)
    except Exception as e:
        print(f"ERRO: {type(e).__name__}: {e}")
        if hasattr(e, '__dict__'):
            print(f"Detalhes: {e.__dict__}")

if __name__ == "__main__":
    asyncio.run(debug_sp())
