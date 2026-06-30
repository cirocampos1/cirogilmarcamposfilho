import sys
import asyncio
from app.fetchers.sofascore import SofascoreFetcher


def fetch_player(player_id, match_id=None):
    fetcher = SofascoreFetcher(match_id=match_id)
    asyncio.run(fetcher.fetch_player(player_id))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python -m app.cli.fetch_player <PLAYER_ID> [MATCH_ID]")
        sys.exit(1)
    player_id = sys.argv[1]
    match_id = sys.argv[2] if len(sys.argv) > 2 else None
    fetch_player(player_id, match_id)
