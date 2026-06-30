from app.utils.business_calendar_helper import BusinessCalendarHelper
from datetime import date

# Teste para Abril 2026
year = 2026
month = 4
info = BusinessCalendarHelper.get_workdays_info(year, month)

print(f"--- Teste Calendário Corporativo () ---")
print(f"Mês: {month}/{year}")
print(f"Total Dias Úteis (Seg-Sáb): {info['total']}")
print(f"Dias Úteis Passados: {info['passed']}")
print(f"Pro-rata (Pace): {info['pace_ratio']:.2%}")
print(f"Dias Restantes: {info['remaining']}")

# Verificar se o arquivo de cache foi criado
import os
cache_path = "app/data/holidays_cache.json"
if os.path.exists(cache_path):
    print(f"\n[OK] Cache criado em: {cache_path}")
    with open(cache_path) as f:
        import json
        cache = json.load(f)
        print(f"Feriados em cache para {year}: {len(cache.get(str(year), []))}")
else:
    print(f"\n[ERRO] Cache não encontrado!")
