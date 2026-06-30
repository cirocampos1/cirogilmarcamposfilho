import asyncio
import json
import os

import sys

MATCH_ID = "15691379"

PLAYER_JSON_FILES = {
    "heatmap": "heatmap.json",
    "shotmap": "shotmap.json",
    "rating_breakdown": "rating_breakdown.json",
    "statistics": "statistics.json",
}


class SofascoreFetcher:
    def __init__(self, match_id=None, output_base=None):
        self.match_id = match_id or MATCH_ID
        self.output_base = output_base or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data"
        )

    async def fetch_player(self, player_id):
        return self.load_player_json(player_id)

    def load_player_json(self, player_id):
        out_dir = os.path.join(self.output_base, f"sofascore_player_{player_id}")
        data = {}
        missing = []

        for name, filename in PLAYER_JSON_FILES.items():
            path = os.path.join(out_dir, filename)
            if not os.path.exists(path):
                missing.append(filename)
                continue

            with open(path, "r", encoding="utf-8") as f:
                data[name] = json.load(f)
            print(f"[OK] JSON local encontrado: {path}")

        if missing:
            print(f"[AVISO] JSONs ausentes em {out_dir}: {', '.join(missing)}")

        return {"player_id": str(player_id), "match_id": str(self.match_id),
                "path": out_dir, "data": data, "missing": missing}


async def fetch_data():
    player_id = sys.argv[1] if len(sys.argv) > 1 else "12345"
    match_id = sys.argv[2] if len(sys.argv) > 2 else MATCH_ID
    fetcher = SofascoreFetcher(match_id=match_id)
    await fetcher.fetch_player(player_id)


if __name__ == "__main__":
    asyncio.run(fetch_data())
