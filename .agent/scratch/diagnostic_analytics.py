import asyncio
import logging
from datetime import date
from app.repositories.sinalsheet_repository import SinalSheetRepository
from app.dependencies.database import get_db

async def diagnostic():
    db = await get_db().__anext__()
    repo = SinalSheetRepository(db)
    
    print("--- Diagnostic: SinalSheet Analytics Data ---")
    
    # 1. Check if tables have data
    count_fila = await db.execute_query("SELECT COUNT(*) as QTD FROM AD_ADSINALSHEETFILA")
    count_log = await db.execute_query("SELECT COUNT(*) as QTD FROM AD_ADSINALSHEETFILALOG")
    
    print(f"Registros em AD_ADSINALSHEETFILA: {count_fila[0][0] if count_fila else 0}")
    print(f"Registros em AD_ADSINALSHEETFILALOG: {count_log[0][0] if count_log else 0}")
    
    # 2. Check a sample of the join
    join_test = await db.execute_query("""
        SELECT TOP 5 l.USERNAME, f.NOME_PROJETO, f.CATEGORIA_TRABALHO, l.HORAS
        FROM AD_ADSINALSHEETFILALOG l
        JOIN AD_ADSINALSHEETFILA f ON f.ID = l.ID_FILA
    """)
    print("\nAmostra de JOIN (Top 5):")
    if join_test:
        for row in join_test:
            print(row)
    else:
        print("Nenhum registro encontrado no JOIN!")

    # 3. Check metadata
    metadata = await repo.get_analytics_filters_metadata()
    print("\nMetadados de Filtros:")
    print(f"Clientes: {len(metadata['clientes'])}")
    print(f"Projetistas: {len(metadata['projetistas'])}")
    print(f"Categorias: {metadata['categorias']}")
    print(f"Especificações: {len(metadata['especificacoes'])}")

    # 4. Check Gamification for today
    today = date.today()
    gamification = await repo.get_designer_gamification(data_inicio=today, data_fim=today)
    print(f"\nGamificação para hoje ({today}): {len(gamification)} registros")

if __name__ == "__main__":
    asyncio.run(diagnostic())
