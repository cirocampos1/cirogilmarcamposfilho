from bs4 import BeautifulSoup

file_path = "/home/leonardobarbosa/dev//docs/vibra/samples/Detalhe do orçamento 1125.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

print("🏷️ Analisando Labels do Cabeçalho...")
for div in soup.find_all("div"):
    text = div.get_text(strip=True)
    if "Engenheiro" in text or "Status" in text or "Localização" in text:
        # Pega o texto e o próximo elemento se for um valor
        print(f"DEBUG: Found text: {text[:100]}")

# Procura especificamente por estruturas de Label + Valor
for span in soup.find_all("span"):
    t = span.get_text(strip=True)
    if ":" in t:
        print(f"Potential Label: {t}")
