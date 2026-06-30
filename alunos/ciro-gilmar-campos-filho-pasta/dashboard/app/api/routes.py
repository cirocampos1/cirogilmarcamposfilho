import json
import os
import subprocess
from fastapi import APIRouter
from app.services.plotter import plot_heatmap, plot_shotmap, plot_passmap
from app.infra.database import DatabaseService

router = APIRouter()

MATCH_ID = "15186850"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
db = DatabaseService()


# ── Helpers ──────────────────────────────────────────────
def data_dir_player(player_id):
    return os.path.join(ROOT, "data", f"sofascore_player_{player_id}")

def data_dir_match(match_id=None):
    m_id = match_id or MATCH_ID
    # Tenta primeiro a pasta bruta da partida
    path = os.path.join(ROOT, "data", "raw", f"match_{m_id}")
    if os.path.exists(path):
        return path
    # Se não existir, tenta usar a pasta sofascore como fallback de lineups/incidents
    return os.path.join(ROOT, "data", "sofascore")

def read_json(*path_parts):
    path = os.path.join(*path_parts)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


# ── API ──────────────────────────────────────────────────
@router.get("/api/players")
def get_players(match_id: int = None):
    """Retorna lista de jogadores (primeiro tenta banco, fallback JSON)."""
    m_id = match_id or int(MATCH_ID)
        
    db_players = db.get_match_players(m_id)
    if db_players:
        players = [{"id": str(p["player_id"]), "name": p["name"]}
                   for p in db_players]
        players = sorted(players, key=lambda x: x["name"] or "")
        return {"players": players}

    match_lineups = os.path.join(data_dir_match(m_id), "lineups.json")
    if os.path.exists(match_lineups):
        with open(match_lineups, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        path = os.path.join(ROOT, "data", "sofascore", "lineups.json")
        if not os.path.exists(path):
            return {"players": []}
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

    players = []
    for team in ("home", "away"):
        for item in data.get(team, {}).get("players", []):
            p = item.get("player", {})
            players.append({"id": str(p.get("id")), "name": p.get("name")})
    players = sorted(players, key=lambda x: x["name"] or "")
    return {"players": players}


@router.get("/api/dashboard-data")
def get_dashboard_data(player_id: str = "866469", match_id: int = None):
    match_id = match_id or int(MATCH_ID)

    # ── 1. Tenta banco de dados (cache) ──
    stats_row = db.get_player_statistics(match_id, player_id)
    heatmap_pts = db.get_heatmap(match_id, player_id)
    shotmap_pts = db.get_shotmap(match_id, player_id)
    events_pass = db.get_player_events(match_id, player_id, "pass")
    events_dribble = db.get_player_events(match_id, player_id, "dribble")
    events_defensive = db.get_player_events(match_id, player_id, "defensive")
    events_carry = db.get_player_events(match_id, player_id, "ball_carry")

    has_maps = bool(heatmap_pts or shotmap_pts or events_pass)
    if stats_row and has_maps:
        return _build_response(stats_row, heatmap_pts, shotmap_pts,
                                events_pass, events_dribble,
                                events_defensive, events_carry)

    # ── 2. Fallback: JSON files ──
    player_dir = data_dir_player(player_id)
    match_dir = data_dir_match(match_id)

    try:
        _ = os.listdir(player_dir)
    except FileNotFoundError:
        print(f"Baixando dados do jogador {player_id}...")
        subprocess.run(
            ["uv", "run", "python", "-m", "app.cli.fetch_player", player_id, str(match_id)],
            cwd=ROOT, timeout=120
        )

    # Heatmap
    hm_raw = (read_json(player_dir, "heatmap.json") or {}).get("heatmap", [])
    if not hm_raw:
        hm_raw = heatmap_pts

    # Shotmap
    sm_raw = (read_json(player_dir, "shotmap.json") or {}).get("shotmap", [])
    if not sm_raw:
        sm2 = read_json(match_dir, f"player_{player_id}_shotmap.json")
        if sm2:
            sm_raw = sm2.get("shotmap", [])

    # Stats
    stats_raw = read_json(match_dir, f"player_{player_id}_stats.json")
    if not stats_raw:
        stats_raw = read_json(player_dir, "player_statistics.json") or read_json(player_dir, "statistics.json")
    
    if stats_raw and isinstance(stats_raw, dict):
        stats_data = stats_raw.get("statistics", stats_raw)
        if not isinstance(stats_data, dict):
            stats_data = {}
    else:
        stats_data = {}

    # Events
    rating_data = read_json(player_dir, "rating_breakdown.json") or {}
    rating_passes = rating_data.get("passes", [])
    if not rating_passes:
        events_file = read_json(match_dir, f"player_{player_id}_events.json") or {}
        rating_passes = events_file.get("passes", [])

    # ── Gera imagens ──
    heatmap_b64 = plot_heatmap(hm_raw)
    shotmap_b64 = plot_shotmap(sm_raw)
    passmap_b64 = plot_passmap(rating_passes)

    # ── Monta stats ──
    def g(key, default=0):
        return stats_data.get(key, default)

    stats_out = {
        "rating": g("rating"),
        "minutesPlayed": g("minutesPlayed"),
        "totalPass": g("totalPass"),
        "accuratePass": g("accuratePass"),
        "totalLongBalls": g("totalLongBalls"),
        "goalAssist": g("goalAssist"),
        "totalCross": g("totalCross"),
        "accurateCross": g("accurateCross"),
        "bigChanceCreated": g("bigChanceCreated"),
        "duelWon": g("duelWon"),
        "duelLost": g("duelLost"),
        "totalTackle": g("totalTackle"),
        "wonTackle": g("wonTackle"),
        "interceptions": g("ballRecovery"),
        "clearances": g("totalClearance"),
        "wasFouled": g("wasFouled"),
        "fouls": g("fouls"),
        "goals": g("goals"),
        "onTargetScoringAttempt": g("onTargetScoringAttempt"),
        "shotOffTarget": g("shotOffTarget"),
        "blockedScoringAttempt": g("blockedScoringAttempt"),
    }

    return {
        "images": {
            "heatmap": heatmap_b64,
            "shotmap": shotmap_b64,
            "passmap": passmap_b64,
        },
        "stats": stats_out,
        "events": {
            "pass": rating_passes[:50],
            "dribble": (rating_data.get("dribbles", []) or [])[:20],
            "defensive": (rating_data.get("defensive", []) or [])[:20],
            "ball_carry": (rating_data.get("ball-carries", []) or [])[:20],
        },
    }


def _build_response(stats_row, heatmap_pts, shotmap_pts,
                    events_pass, events_dribble,
                    events_defensive, events_carry):
    """Constrói resposta a partir de dados do banco."""
    def to_events(raw_list, db_type):
        return [
            {
                "playerCoordinates": {"x": e["x"], "y": e["y"]},
                "passEndCoordinates": {"x": e.get("end_x", 0), "y": e.get("end_y", 0)},
                "outcome": bool(e["outcome"]),
                "keypass": bool(e["keypass"]),
                "isHome": bool(e["is_home"]),
            }
            for e in raw_list if e.get("x") is not None
        ]

    def format_shotmap(raw_shots):
        return [
            {
                "playerCoordinates": {"x": s["x"], "y": s["y"]},
                "shotType": s["shotType"]
            }
            for s in raw_shots if s.get("x") is not None
        ]

    heatmap_b64 = plot_heatmap(heatmap_pts)
    shotmap_b64 = plot_shotmap(format_shotmap(shotmap_pts))
    passmap_b64 = plot_passmap(to_events(events_pass, "pass"))

    return {
        "images": {
            "heatmap": heatmap_b64,
            "shotmap": shotmap_b64,
            "passmap": passmap_b64,
        },
        "stats": {
            "rating": stats_row.get("rating", 0),
            "minutesPlayed": stats_row.get("minutesPlayed", 0),
            "totalPass": stats_row.get("total_pass", 0),
            "accuratePass": stats_row.get("accurate_pass", 0),
            "goalAssist": stats_row.get("goal_assist", 0),
            "totalCross": stats_row.get("total_cross", 0),
            "accurateCross": stats_row.get("accurate_cross", 0),
            "bigChanceCreated": stats_row.get("big_chance_created", 0),
            "duelWon": stats_row.get("duel_won", 0),
            "duelLost": stats_row.get("duel_lost", 0),
            "totalTackle": stats_row.get("total_tackle", 0),
            "wonTackle": stats_row.get("won_tackle", 0),
            "interceptions": stats_row.get("ball_recovery", 0),
            "clearances": stats_row.get("total_clearance", 0),
            "wasFouled": stats_row.get("was_fouled", 0),
            "fouls": stats_row.get("fouls", 0),
            "goals": stats_row.get("goals", 0),
            "onTargetScoringAttempt": stats_row.get("on_target_scoring_attempt", 0),
            "shotOffTarget": stats_row.get("shot_off_target", 0),
            "blockedScoringAttempt": stats_row.get("blocked_scoring_attempt", 0),
        },
        "events": {
            "pass": to_events(events_pass, "pass")[:50],
            "dribble": to_events(events_dribble, "dribble")[:20],
            "defensive": to_events(events_defensive, "defensive")[:20],
            "ball_carry": to_events(events_carry, "ball_carry")[:20],
        },
    }


@router.get("/api/matches")
def list_matches():
    matches = db.list_matches(20)
    # Garante que a partida da França vs Irlanda do Norte (16130149) esteja disponível
    if not any(m["match_id"] == 16130149 for m in matches):
        matches.append({
            "match_id": 16130149,
            "home_team": "França",
            "away_team": "Irlanda do Norte",
            "match_date": "2026-06-08",
            "competition": "Amistoso Internacional"
        })
    return {"matches": matches}


@router.get("/api/players/db")
def list_players_db():
    return {"players": db.list_players(200)}
