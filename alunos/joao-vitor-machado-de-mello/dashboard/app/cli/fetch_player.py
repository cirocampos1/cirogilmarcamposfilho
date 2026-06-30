import sys
import asyncio
from app.fetchers.sofascore import SofascoreFetcher


def fetch_player(player_id, match_id=None):
    fetcher = SofascoreFetcher(match_id=match_id)
    result = asyncio.run(fetcher.fetch_player(player_id))
    found = sorted(result["data"].keys())
    missing = result["missing"]
    print(f"Jogador {player_id} | encontrados: {found or 'nenhum'}")
    if missing:
        print(f"Arquivos pendentes: {missing}")
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python -m app.cli.fetch_player <PLAYER_ID> [MATCH_ID]")
        print("Lê JSONs locais em data/sofascore_player_<PLAYER_ID>/; não acessa a rede.")
        sys.exit(1)
    player_id = sys.argv[1]
    match_id = sys.argv[2] if len(sys.argv) > 2 else None
    fetch_player(player_id, match_id)
