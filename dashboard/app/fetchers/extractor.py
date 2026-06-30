import os
import json
import time
import logging
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SofascoreExtractor:
    def __init__(self, delay: float = 2.0):
        self.base_url = 'https://www.sofascore.com/api/v1'
        self.delay = delay

    def download_match_data(self, match_id: int, output_dir: str):
        match_dir = os.path.join(output_dir, f"match_{match_id}")
        os.makedirs(match_dir, exist_ok=True)

        logger.info(f"Iniciando Undetected ChromeDriver para o jogo {match_id}...")

        options = uc.ChromeOptions()
        driver = uc.Chrome(options=options)

        try:
            logger.info("Acessando a página principal para obter cookies do Cloudflare...")
            driver.get('https://www.sofascore.com/')
            time.sleep(5)  # tempo para carregar e passar no Cloudflare da home

            def fetch_api(endpoint: str):
                url = f"{self.base_url}/{endpoint}"
                driver.get(url)
                time.sleep(self.delay)
                try:
                    content = driver.find_element(By.TAG_NAME, "pre").text
                    if not content:
                        content = driver.find_element(By.TAG_NAME, "body").text
                    return json.loads(content)
                except Exception as e:
                    logger.error(f"Erro ao parsear JSON de {url}: {e}")
                    return None

            logger.info(f"Coletando escalações para a partida {match_id}")
            lineups = fetch_api(f"event/{match_id}/lineups")

            if not lineups or 'error' in lineups:
                logger.error(f"Falha ao obter escalações. Retorno: {lineups}. Abortando extração.")
                return

            with open(os.path.join(match_dir, "lineups.json"), 'w', encoding='utf-8') as f:
                json.dump(lineups, f, ensure_ascii=False, indent=4)

            player_ids = set()
            for team in ['home', 'away']:
                team_data = lineups.get(team, {})
                for squad_type in ['players', 'missingPlayers']:
                    for p in team_data.get(squad_type, []):
                        player = p.get('player', {})
                        p_id = player.get('id')
                        if p_id:
                            player_ids.add(p_id)

            player_ids = list(set(player_ids))
            total_players = len(player_ids)
            logger.info(f"Encontrados {total_players} jogadores na partida. Iniciando iteração...")

            for i, player_id in enumerate(player_ids, 1):
                logger.info(f"[{i}/{total_players}] Processando jogador ID: {player_id}")

                stats_data = fetch_api(f"event/{match_id}/player/{player_id}/statistics")
                if stats_data and 'error' not in stats_data:
                    with open(os.path.join(match_dir, f"player_{player_id}_stats.json"), 'w', encoding='utf-8') as f:
                        json.dump(stats_data, f, ensure_ascii=False, indent=2)

                shotmap_data = fetch_api(f"event/{match_id}/shotmap/player/{player_id}")
                if shotmap_data and 'error' not in shotmap_data and shotmap_data.get('shotmap'):
                    with open(os.path.join(match_dir, f"player_{player_id}_shotmap.json"), 'w', encoding='utf-8') as f:
                        json.dump(shotmap_data, f, ensure_ascii=False, indent=2)

                rating_data = fetch_api(f"event/{match_id}/player/{player_id}/rating-breakdown")
                if rating_data and 'error' not in rating_data:
                    with open(os.path.join(match_dir, f"player_{player_id}_rating.json"), 'w', encoding='utf-8') as f:
                        json.dump(rating_data, f, ensure_ascii=False, indent=2)

            logger.info(f"Extração da partida {match_id} concluída com sucesso!")
        finally:
            driver.quit()

if __name__ == "__main__":
    extractor = SofascoreExtractor(delay=2.0)
    JOGO_ID = 15186850
    OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'raw')
    extractor.download_match_data(JOGO_ID, OUTPUT_DIR)
