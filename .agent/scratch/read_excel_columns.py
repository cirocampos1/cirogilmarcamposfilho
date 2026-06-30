import pandas as pd
try:
    df = pd.read_excel("app/data/vibra/relatorio_geral_clean.xlsx", header=4)
    print("Colunas encontradas:")
    for col in df.columns:
        print(f"- {col}")
except Exception as e:
    print(f"Erro: {e}")
