import soccerdata as sd
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
from pathlib import Path
import sqlite3

def setup_directories():
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    parquet_dir = data_dir / "parquet"
    data_dir.mkdir(parents=True, exist_ok=True)
    parquet_dir.mkdir(parents=True, exist_ok=True)
    return data_dir, parquet_dir

def main():
    data_dir, parquet_dir = setup_directories()
    print("Iniciando extração do FBref usando soccerdata...")
    
    # Criando o scraper para o Brasileirão Série A (usando a temporada de 2026 como exemplo consistente)
    try:
        fbref = sd.FBref(leagues="BRA-Serie A", seasons="2025")
        
        # 1. Partidas e Resultados
        print("Extraindo resultados das partidas (Calendário)...")
        schedule = fbref.read_schedule()
        schedule.to_parquet(parquet_dir / "schedule.parquet")
        
        # 2. Estatísticas das Equipes na Temporada (Stats standards)
        print("Extraindo estatísticas padrão das equipes...")
        team_stats = fbref.read_team_season_stats(stat_type="standard")
        team_stats.to_parquet(parquet_dir / "team_stats.parquet")
        
        # 3. Estatísticas de Jogadores na Temporada
        print("Extraindo estatísticas padrão dos jogadores...")
        player_stats = fbref.read_player_season_stats(stat_type="standard")
        player_stats.to_parquet(parquet_dir / "player_stats.parquet")
        
        print("Arquivos Parquet gerados com sucesso na pasta data/parquet/")
        
        # Opcional: Salvando num banco SQLite para uso em Dashboards rápidos
        print("Exportando para SQLite...")
        conn = sqlite3.connect(data_dir / "fbref_brasileirao.db")
        schedule.to_sql("schedule", conn, if_exists="replace")
        team_stats.to_sql("team_stats", conn, if_exists="replace")
        player_stats.to_sql("player_stats", conn, if_exists="replace")
        conn.close()
        print("Banco de dados SQLite (fbref_brasileirao.db) gerado com sucesso!")
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\n[ERRO] Ocorreu um problema durante a extração: {e}")
        print("Dica: Se foi um erro HTTP 403/429, o limite de requisições do FBref pode ter sido excedido.")
        print("Verifique se o cache do soccerdata está ativo ou aguarde algumas horas.")

if __name__ == "__main__":
    main()
