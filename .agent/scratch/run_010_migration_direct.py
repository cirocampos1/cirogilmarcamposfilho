import os
import pyodbc
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

conn_str = os.getenv("PRIORIZACAO_DIRECT_READ_CONNECTION_STRING")
if not conn_str:
    print("Erro: PRIORIZACAO_DIRECT_READ_CONNECTION_STRING não encontrada no .env")
    exit(1)

# Remove aspas se houver
conn_str = conn_str.strip('"')

def run_sql_script(filename):
    try:
        print(f"Conectando ao banco de dados...")
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        print(f"Lendo script: {filename}")
        with open(filename, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        # O pyodbc não suporta 'GO', precisamos dividir o script
        commands = sql_script.split('GO')
        
        for cmd in commands:
            cmd = cmd.strip()
            if cmd:
                print(f"Executando comando...")
                cursor.execute(cmd)
        
        conn.commit()
        print("Migração concluída com sucesso!")
        
    except Exception as e:
        print(f"Erro durante a migração: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    run_sql_script("sql/010_sinalsheet_queue_tables.sql")
