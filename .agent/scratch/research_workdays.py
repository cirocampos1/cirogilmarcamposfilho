import requests
from datetime import date, timedelta
import calendar

def get_holidays(year):
    url = f"https://brasilapi.com.br/api/feriados/v1/{year}"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            return [h['date'] for h in resp.json()]
    except:
        pass
    return []

def calculate_workdays(year, month, holidays):
    """Calcula dias úteis (Seg-Sab) em um mês, excluindo feriados."""
    first_day = date(year, month, 1)
    last_day = date(year, month, calendar.monthrange(year, month)[1])
    
    total_workdays = 0
    workdays_so_far = 0
    today = date.today()
    
    curr = first_day
    while curr <= last_day:
        # Sábado é o dia 5 no weekday() (Seg=0, Sab=5, Dom=6)
        is_weekend = curr.weekday() == 6 # Domingo
        is_holiday = curr.strftime("%Y-%m-%d") in holidays
        
        if not is_weekend and not is_holiday:
            total_workdays += 1
            if curr <= today:
                workdays_so_far += 1
        
        curr += timedelta(days=1)
        
    return total_workdays, workdays_so_far

# Teste para Abril 2026
year = 2026
month = 4
holidays = get_holidays(year)
total, so_far = calculate_workdays(year, month, holidays)

print(f"Ano: {year}, Mes: {month}")
print(f"Feriados encontrados: {len(holidays)}")
print(f"Total dias úteis (Seg-Sab): {total}")
print(f"Dias úteis até hoje: {so_far}")
print(f"Pro-rata real: {so_far/total:.2%}")
