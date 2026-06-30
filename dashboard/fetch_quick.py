import os
import json
from curl_cffi import requests
import time

match_id = 15186850
output_dir = os.path.join(os.path.dirname(__file__), 'app', 'data', 'raw', f'match_{match_id}')
os.makedirs(output_dir, exist_ok=True)

headers = {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "baggage": "sentry-environment=production,sentry-public_key=d693747a6bb242d9bb9cf7069fb57988,sentry-trace_id=2845103e37c1517ef00ecbdfce6ae213,sentry-org_id=18522,sentry-sample_rand=0.06093940029075928",
    "cache-control": "max-age=0",
    "cookie": "AD_VERGE_SESSION_COOKIE_V1=59949c41-d906-47ce-981a-69157df7e4bb; _cc_id=6bd656a16fd44dd0de245e537ee6ec9d; _gcl_au=1.1.1571646141.1774181159; _ga=GA1.1.1886594496.1774181159; _adv_sid=01446719-4e78-4278-a65a-e26e59ad44d0; ssp_test=control; cto_bundle=Lo8KXV9Fdm9MOUVGd0x2NG5NU1k0cXcwdWloM3g0anVublFkZ0xlNThxbzV2SiUyQk1mUXVxcDNwc2pnNkhJY1h1bWJLWjR0ZEFodHFKdEpOckRvS3JxaTU0eCUyQkRnRlRUQjBreWpvSk11b29DckpGOEhhcHVBSm43WW1lSWRreWdNViUyQjFxdm9JbUxBbk0lMkZpWndoY0IzZU1kZWdvdyUzRCUzRA; cto_bidid=sZjLL19LWVVaMUVMTGslMkJQcFhrSXY5ZWglMkJUWU5VWWduMEtXSzVFdWFGdWViUnJvMjFORXZTZmZ3V2NwMWtES09pcyUyRjh3MGJXbHFTZkRnbUROU2o3eHMlMkZqcGVZWmJsdHQ5UVppbElxRzJYUDcwTFp3JTNE; __gads=ID=f61254e7abc2828d:T=1756383691:RT=1781559747:S=ALNI_MYZYxRndqXwr36likf4plKetffd-g; __gpi=UID=00001275b08fff09:T=1756383691:RT=1781559747:S=ALNI_MYIGJwsICNyh7wP1Qn4PFzSqPNfBw; __eoi=ID=712dbfff31b5bb55:T=1774181158:RT=1781559747:S=AA-AfjZOo47c1Xsz6SAj9ciKFW8I; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%2202438768-2f7f-4ee4-a19f-1820e90c1322%5C%22%2C%5B1774181157%2C658000000%5D%5D%22%5D%5D%5D; FCNEC=%5B%5B%22AKsRol83A5obUj0AYbHHYluFFbP5uS2n1YU7rsKvt_5Bgb4Ta0vHI92-KX8hT3nlFhZKy0b6SWe6puke7fNWbDuKwXijDIJDwJL_38dcf62zrgsrU02WHT_QtHkWgW_Mdu2UjZ2StgS_DsvAFr83qxA87oxbeWE9Bw%3D%3D%22%5D%5D; _ga_HNQ9P9MGZR=GS2.1.s1781559751$o10$g1$t1781560085$j33$l0$h0",
    "if-none-match": "W/\"9cdbe3185d\"",
    "priority": "u=1, i",
    "referer": "https://www.sofascore.com/pt/football/match/morocco-brazil/YUbsDVb",
    "sec-ch-ua": "\"Google Chrome\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sentry-trace": "2845103e37c1517ef00ecbdfce6ae213-bf72ac9290e4283d",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "x-requested-with": "492313"
}

def fetch(url, filename):
    time.sleep(0.5)
    try:
        r = requests.get(url, headers=headers, impersonate="chrome110")
        if r.status_code == 200:
            with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                f.write(r.text)
            return r.json()
        elif r.status_code == 304:
            # Not modified, ignore
            pass
        else:
            print(f"Failed {url}: {r.status_code} {r.text[:100]}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

print("Fetching lineups...")
lineups = fetch(f"https://www.sofascore.com/api/v1/event/{match_id}/lineups", "lineups.json")

if lineups:
    player_ids = set()
    for team in ['home', 'away']:
        for squad in ['players', 'missingPlayers']:
            for p in lineups.get(team, {}).get(squad, []):
                pid = p.get('player', {}).get('id')
                if pid:
                    player_ids.add(pid)
    
    total = len(player_ids)
    print(f"Found {total} players.")
    for i, pid in enumerate(player_ids, 1):
        print(f"Fetching player {i}/{total} ID: {pid}")
        fetch(f"https://www.sofascore.com/api/v1/event/{match_id}/player/{pid}/statistics", f"player_{pid}_stats.json")
        fetch(f"https://www.sofascore.com/api/v1/event/{match_id}/shotmap/player/{pid}", f"player_{pid}_shotmap.json")
        fetch(f"https://www.sofascore.com/api/v1/event/{match_id}/player/{pid}/rating-breakdown", f"player_{pid}_rating.json")

print("Done!")
