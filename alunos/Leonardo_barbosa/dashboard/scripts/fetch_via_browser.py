"""Fetch match data by loading the SofaScore page and intercepting API responses."""
import json
import os
import time
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(ROOT, 'data', 'raw')
sys.path.insert(0, os.path.join(ROOT, 'app'))


def fetch_match(match_id: int, page_url: str = None):
    match_dir = os.path.join(OUTPUT_DIR, f"match_{match_id}")
    os.makedirs(match_dir, exist_ok=True)
    print(f"Output: {match_dir}")

    from playwright.sync_api import sync_playwright

    captured = {}

    def filename_for(url: str):
        if not url.startswith('https://api.sofascore.com/api/v1/'):
            return None
        endpoint = url[39:]
        parts = endpoint.split('/')

        # Match-level
        if endpoint == f'event/{match_id}': return 'match_info.json'
        if endpoint == f'event/{match_id}/incidents': return 'incidents.json'
        if endpoint == f'event/{match_id}/statistics': return 'match_statistics.json'
        if endpoint == f'event/{match_id}/lineups': return 'lineups.json'
        if endpoint == f'event/{match_id}/average-positions': return 'average_positions.json'

        # Per-player
        if len(parts) >= 5 and parts[0] == 'event' and parts[1] == str(match_id):
            if parts[2] == 'player' and parts[4] == 'statistics':
                return f'player_{parts[3]}_stats.json'
            if parts[2] == 'shotmap' and parts[3] == 'player':
                return f'player_{parts[4]}_shotmap.json'
            if parts[2] == 'player' and parts[4] == 'rating-breakdown':
                return f'player_{parts[3]}_rating.json'

        # Unique match endpoints
        if parts[0] == 'unique-tournament' or parts[0] == 'team':
            return None  # skip these

        return None

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            locale='pt-BR',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        )
        page = ctx.new_page()

        def on_resp(response):
            url = response.url
            fn = filename_for(url)
            if not fn or fn in captured:
                return
            if response.status != 200:
                return
            try:
                data = response.json()
                captured[fn] = True
                with open(os.path.join(match_dir, fn), 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f'  + {fn}')
            except Exception:
                pass

        page.on('response', on_resp)

        # If no URL provided, try to find it
        if not page_url:
            page_url = f'https://www.sofascore.com/#id:{match_id}'

        print(f'Navigating: {page_url}')
        try:
            page.goto(page_url, wait_until='domcontentloaded', timeout=120000)
            print('Page loaded, waiting for API responses...')
            time.sleep(12)
        except Exception as e:
            print(f'Page load issue: {e}')
            time.sleep(5)

        print(f'Captured {len(captured)} files')
        for fn in sorted(captured):
            print(f'  - {fn}')

        # If we got lineups, fetch per-player by visiting player pages
        lineups_file = os.path.join(match_dir, 'lineups.json')
        if os.path.exists(lineups_file):
            with open(lineups_file, 'r') as f:
                lineups = json.load(f)
            player_ids = set()
            for team in ('home', 'away'):
                for item in lineups.get(team, {}).get('players', []):
                    pid = item.get('player', {}).get('id')
                    if pid:
                        player_ids.add(pid)
            player_ids = sorted(player_ids)
            print(f'{len(player_ids)} players found. Visiting pages...')
            for i, pid in enumerate(player_ids, 1):
                print(f'  [{i}/{len(player_ids)}] player {pid}')
                try:
                    page.goto(
                        f'https://www.sofascore.com/player/{pid}',
                        wait_until='domcontentloaded',
                        timeout=30000
                    )
                    time.sleep(1.5)
                except Exception as e:
                    print(f'    error: {e}')
        else:
            print('No lineups.json captured')

        browser.close()
        print(f'Done! Total files: {len(captured)}')


if __name__ == '__main__':
    mid = int(sys.argv[1]) if len(sys.argv) > 1 else 15186502
    url = sys.argv[2] if len(sys.argv) > 2 else None
    fetch_match(mid, url)
