import asyncio
import os
import json
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.core.config import settings

async def main():
    token_provider = SankhyaTokenProvider()
    client = SankhyaGatewayClient(token_provider)
    
    # Query para buscar tabelas no INFORMATION_SCHEMA
    query = "SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'AD_SINAL_SHEET%'"
    payload = {"sql": query}
    
    try:
        print("Buscando tabelas no banco...")
        resp = await client.call("DbExplorerSP.executeQuery", payload)
        
        # O retorno do DbExplorer no Sankhya geralmente é {"rows": [[schema, name], ...], "fields": [...]}
        print("Resposta do Sankhya:")
        print(json.dumps(resp, indent=2))
        
        # Testar se as tabelas de fila estão acessíveis
        tabelas_alvo = ['AD_SINAL_SHEET_FILA', 'AD_SINAL_SHEET_FILA_LOG']
        for tab in tabelas_alvo:
            print(f"\nTestando acesso à tabela {tab}...")
            
            # Tentar com prefixo sankhya.
            try:
                res = await client.call("DbExplorerSP.executeQuery", {"sql": f"SELECT TOP 1 * FROM sankhya.{tab}"})
                print(f"Sucesso ao ler sankhya.{tab}")
            except Exception as e:
                print(f"Falha ao ler sankhya.{tab}: {e}")
                
            # Tentar sem prefixo
            try:
                res = await client.call("DbExplorerSP.executeQuery", {"sql": f"SELECT TOP 1 * FROM {tab}"})
                print(f"Sucesso ao ler {tab} (sem prefixo)")
            except Exception as e:
                print(f"Falha ao ler {tab} (sem prefixo): {e}")

    except Exception as e:
        print(f"Erro ao executar busca: {e}")

if __name__ == "__main__":
    asyncio.run(main())
