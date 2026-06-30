import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()
conn_str = os.getenv("PRIORIZACAO_DIRECT_READ_CONNECTION_STRING").strip('"')

try:
    print("Testando conexão direta...")
    conn = pyodbc.connect(conn_str, timeout=5)
    print("Conexão OK!")
    conn.close()
except Exception as e:
    print(f"Erro de conexão: {e}")
