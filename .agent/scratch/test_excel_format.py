import pandas as pd
import sys

file_path = '/home/leonardobarbosa/dev//docs/vibra/Orcamento_Prosp_GILMAR NIQUINI & FILHOS EMPREENDIMENTOS LTDA_1125_02052026.xlsx'

print(f"--- Testando arquivo: {file_path} ---")

# Teste 1: HTML
try:
    dfs = pd.read_html(file_path)
    print(f"✅ Sucesso como HTML! {len(dfs)} tabelas encontradas.")
    print(dfs[0].head())
except Exception as e:
    print(f"❌ Falha como HTML: {e}")

# Teste 2: XML (lxml)
try:
    df = pd.read_xml(file_path)
    print("✅ Sucesso como XML!")
    print(df.head())
except Exception as e:
    print(f"❌ Falha como XML: {e}")

# Teste 3: Pandas normal com tratamento de cores via openpyxl manual
try:
    import openpyxl
    wb = openpyxl.load_workbook(file_path, data_only=True)
    sheet = wb.active
    print(f"✅ Sucesso via openpyxl manual! Planilha: {sheet.title}")
    for row in sheet.iter_rows(max_row=5, values_only=True):
        print(row)
except Exception as e:
    print(f"❌ Falha via openpyxl: {e}")
