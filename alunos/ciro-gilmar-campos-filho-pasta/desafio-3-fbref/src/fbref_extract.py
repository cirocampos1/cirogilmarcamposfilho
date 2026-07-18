import ast
import sqlite3
from pathlib import Path
import pandas as pd

def setup_directories():
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    parquet_dir = data_dir / "parquet"
    data_dir.mkdir(parents=True, exist_ok=True)
    parquet_dir.mkdir(parents=True, exist_ok=True)
    return data_dir, parquet_dir

def restore_tuple_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Reconstroi colunas MultiIndex que o SQLite achatou em strings como "('Performance', 'Gls')"."""
    parsed = [ast.literal_eval(c) if isinstance(c, str) and c.startswith("(") else c for c in df.columns]
    if any(isinstance(c, tuple) for c in parsed):
        df.columns = pd.MultiIndex.from_tuples(c if isinstance(c, tuple) else (c, "") for c in parsed)
    return df

def load_table(conn: sqlite3.Connection, table_name: str, index_cols: list[str]) -> pd.DataFrame:
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    df = restore_tuple_columns(df)
    return df.set_index(index_cols)

def main():
    data_dir, parquet_dir = setup_directories()
    db_path = data_dir / "fbref_brasileirao.db"

    # O FBref bloqueia raspagens automatizadas com frequência (CAPTCHA/IP block),
    # então em vez de raspar ao vivo a cada execução, reconstruímos os parquets
    # a partir do banco local (dado semente do desafio, já extraído do FBref).
    print(f"Reconstruindo parquets a partir de {db_path}...")

    conn = sqlite3.connect(db_path)
    try:
        schedule = load_table(conn, "schedule", ["league", "season", "game"])
        team_stats = load_table(conn, "team_stats", ["league", "season", "team"])
        player_stats = load_table(conn, "player_stats", ["league", "season", "team", "player"])
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\n[ERRO] Ocorreu um problema ao carregar do banco local: {e}")
        return
    finally:
        conn.close()

    schedule.to_parquet(parquet_dir / "schedule.parquet")
    team_stats.to_parquet(parquet_dir / "team_stats.parquet")
    player_stats.to_parquet(parquet_dir / "player_stats.parquet")

    print(f"Calendário: {len(schedule)} jogos | Times: {len(team_stats)} | Jogadores: {len(player_stats)}")
    print("Parquets gerados com sucesso em data/parquet/ a partir do banco local.")

if __name__ == "__main__":
    main()
