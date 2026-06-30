
import sys
import os
import asyncio

# Adiciona o diretório raiz ao path para importar as dependências
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.dependencies.sankhya import get_db_repository

async def find_tables():
    repo = get_db_repository()
    
    # Busca por tabelas físicas no banco (independente do dicionário)
    sql = "SELECT s.name as schema_name, t.name as table_name FROM sys.tables t JOIN sys.schemas s ON t.schema_id = s.schema_id WHERE t.name LIKE '%SINAL%' OR t.name LIKE '%SHEET%'"
    
    try:
        res = await repo.execute_query(sql)
        rows = repo.to_rows(res)
        print("--- Tabelas Físicas Encontradas ---")
        for r in rows:
            print(f"- {r['schema_name']}.{r['table_name']}")
    except Exception as e:
        print(f"Erro ao buscar tabelas: {e}")

if __name__ == "__main__":
    asyncio.run(find_tables())
