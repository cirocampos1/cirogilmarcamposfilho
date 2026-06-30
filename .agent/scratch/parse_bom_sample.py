import os
from bs4 import BeautifulSoup

file_path = "/home/leonardobarbosa/dev//docs/vibra/samples/Detalhe do orçamento 1125.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

print("🔍 Analisando Detalhe do Orçamento...")

# 1. Cabeçalho (Engenheiro, etc)
header_info = soup.find("div", class_="budget-detail-header")
if header_info:
    print(f"Header: {header_info.get_text(strip=True, separator=' | ')}")

# 2. Tabela de Itens (BOM)
table = soup.find("table", class_="cs-table")
if not table:
    # Procura por qualquer tabela se a classe cs-table falhar
    table = soup.find("table")

if table:
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    print(f"Colunas: {headers}")
    
    rows = table.find_all("tr", class_=lambda x: x and "cs-row-table-summary" in x)
    if rows:
        first_row = rows[0]
        cells = first_row.find_all("td")
        for i, cell in enumerate(cells):
            h = headers[i] if i < len(headers) else f"Col_{i}"
            print(f"  {h}: {cell.get_text(strip=True)}")
    else:
        print("❌ Nenhuma linha 'cs-row-table-summary' encontrada.")
else:
    print("❌ Tabela não encontrada no HTML.")
