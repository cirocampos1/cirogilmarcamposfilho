"""Fetch full match data from SofaScore via undetected_chromedriver.

Usage:
    uv run python scripts/fetch_match_data.py 15186502
"""
import os
import json
import time
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = 'https://www.sofascore.com/api/v1'
ROOT = os.path.dirname(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(ROOT, 'data', 'raw')
sys.path.insert(0, os.path.join(ROOT, 'app'))


def fetch_match(match_id: int):
    match_dir = os.path.join(OUTPUT_DIR, f"match_{match_id}")
    os.makedirs(match_dir, exist_ok=True)
    logger.info(f"Partida {match_id} -> {match_dir}")

    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By

    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")

    driver = uc.Chrome(options=options, version_main=149)

    try:
        logger.info("Acessando sofascore.com...")
        driver.get('https://www.sofascore.com/')
        time.sleep(5)

        def fetch_api(endpoint: str, filename: str):
            url = f"{BASE_URL}/{endpoint}"
            logger.info(f"Fetching {url}")
            driver.get(url)
            time.sleep(1.5)
            try:
                body = driver.find_element(By.TAG_NAME, "pre").text
                if not body:
                    body = driver.find_element(By.TAG_NAME, "body").text
                data = json.loads(body)
                if 'error' not in data:
                    filepath = os.path.join(match_dir, filename)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    logger.info(f"  -> OK {filename}")
                    return data
                else:
                    logger.warning(f"  -> Erro API: {data['error'].get('reason', data['error'])}")
            except Exception as e:
                logger.error(f"  -> Falha {filename}: {e}")
            return None

        # 1. Match info
        fetch_api(f"event/{match_id}", "match_info.json")

        # 2. Incidents (gols, cartoes, substituicoes, VAR)
        fetch_api(f"event/{match_id}/incidents", "incidents.json")

        # 3. Match statistics (posse, chutes, etc)
        fetch_api(f"event/{match_id}/statistics", "match_statistics.json")

        # 4. Lineups
        lineups = fetch_api(f"event/{match_id}/lineups", "lineups.json")
        if not lineups:
            logger.error("Sem lineups, abortando extracao individual.")
            driver.quit()
            return

        player_ids = set()
        for team in ['home', 'away']:
            team_data = lineups.get(team, {})
            for squad_type in ['players', 'missingPlayers']:
                for p in team_data.get(squad_type, []):
                    pid = p.get('player', {}).get('id')
                    if pid:
                        player_ids.add(pid)

        player_ids = sorted(player_ids)
        total = len(player_ids)
        logger.info(f"{total} jogadores encontrados.")

        for i, pid in enumerate(player_ids, 1):
            logger.info(f"[{i}/{total}] Jogador {pid}")
            fetch_api(f"event/{match_id}/player/{pid}/statistics", f"player_{pid}_stats.json")
            fetch_api(f"event/{match_id}/shotmap/player/{pid}", f"player_{pid}_shotmap.json")
            fetch_api(f"event/{match_id}/player/{pid}/rating-breakdown", f"player_{pid}_rating.json")

        # 5. Average positions
        fetch_api(f"event/{match_id}/average-positions", "average_positions.json")

        logger.info(f"Partida {match_id} concluida!")

    finally:
        driver.quit()


def persist_match_data(match_id: int):
    from infra.persist import ingest_match_data
    from infra.database import DatabaseService
    db = DatabaseService()
    ingest_match_data(db, str(match_id))
    logger.info("Persistencia concluida!")


if __name__ == "__main__":
    mid = int(sys.argv[1]) if len(sys.argv) > 1 else 15186502
    if "--persist-only" in sys.argv:
        persist_match_data(mid)
    elif "--fetch-only" in sys.argv:
        fetch_match(mid)
    else:
        fetch_match(mid)
        persist_match_data(mid)
