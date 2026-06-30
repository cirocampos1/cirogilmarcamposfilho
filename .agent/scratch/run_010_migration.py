import asyncio
import os
import sys
from unittest.mock import MagicMock

# Adiciona o diretório atual ao path para importar os módulos do app
sys.path.append(os.getcwd())

from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def run_migration():
    # Mock do gateway pois o DbExplorerRepository usa apenas para logs ou fallback no código,
    # mas o execute_query usa o client de banco configurado.
    # Nota: Precisamos carregar as configs do .env
    from app.core.config import settings
    
    repo = SankhyaDbExplorerRepository(gateway=MagicMock())
    
    with open("sql/010_sinalsheet_queue_tables.sql", "r") as f:
        sql = f.read()
    
    # Divide por batches se houver GO ou apenas executa o bloco
    # O DbExplorer geralmente aceita blocos.
    print("Executando migração das tabelas de fila...")
    try:
        # Removendo GO para compatibilidade com execução direta via driver
        sql_clean = sql.replace("GO", "")
        resp = await repo.execute_query(sql_clean)
        print("Migração concluída com sucesso.")
        print(resp)
    except Exception as e:
        print(f"Erro ao executar migração: {e}")

if __name__ == "__main__":
    asyncio.run(run_migration())
