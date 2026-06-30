import json
import os
import glob
from copy import deepcopy
from time import monotonic
from fastapi import APIRouter
from app.services.plotter import plot_heatmap, plot_shotmap, plot_passmap
from app.infra.database import DatabaseService

router = APIRouter()

MATCH_ID = "15691379"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
db = DatabaseService()
CACHE_TTL_SECONDS = 60
_cache = {}


# ── Helpers ──────────────────────────────────────────────
def data_dir_player(player_id):
    return os.path.join(ROOT, "data", f"sofascore_player_{player_id}")


def normalize_match_id(match_id=None):
    return str(match_id or MATCH_ID)


def data_dir_match(match_id=None):
    return os.path.join(ROOT, "data", "raw", f"match_{normalize_match_id(match_id)}")

def read_json(*path_parts):
    path = os.path.join(*path_parts)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def first_json(*paths):
    for path in paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    return None


def get_cache(key):
    item = _cache.get(key)
    if not item:
        return None
    if monotonic() - item["created_at"] > CACHE_TTL_SECONDS:
        return None
    return deepcopy(item["value"])


def set_cache(key, value):
    _cache[key] = {"created_at": monotonic(), "value": deepcopy(value)}
    return value


def list_local_match_ids():
    match_ids = {MATCH_ID}
    raw_base = os.path.join(ROOT, "data", "raw")
    for path in glob.glob(os.path.join(raw_base, "match_*")):
        if os.path.isdir(path):
            match_ids.add(os.path.basename(path).replace("match_", ""))
    for match in db.list_matches(200):
        match_ids.add(str(match["match_id"]))
    return sorted(match_ids)


def read_lineups(match_id):
    match_lineups = os.path.join(data_dir_match(match_id), "lineups.json")
    if os.path.exists(match_lineups):
        with open(match_lineups, "r", encoding="utf-8") as f:
            return json.load(f)

    legacy_path = os.path.join(ROOT, "data", "sofascore", "lineups.json")
    if normalize_match_id(match_id) == MATCH_ID and os.path.exists(legacy_path):
        with open(legacy_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def players_from_lineups(match_id):
    data = read_lineups(match_id) or {}
    players = []
    for team in ("home", "away"):
        for item in data.get(team, {}).get("players", []):
            p = item.get("player", {})
            if p.get("id") is not None:
                players.append({"id": str(p.get("id")), "name": p.get("name")})
    return players


def is_generic_team_name(name):
    return not name or str(name).strip().lower() in {"home", "away"}


def team_name_from_lineup_side(lineup_side):
    side = lineup_side or {}
    direct_name = side.get("name") or side.get("team", {}).get("name")
    if direct_name:
        return direct_name

    names = {}
    for item in side.get("players", []):
        player = item.get("player", {})
        country = player.get("country", {})
        name = country.get("name") or country.get("shortName")
        if name:
            names[name] = names.get(name, 0) + 1

    if not names:
        return None
    return max(names.items(), key=lambda entry: entry[1])[0]


def resolve_match_team_name(db_name, lineup_side, fallback):
    inferred_name = team_name_from_lineup_side(lineup_side)
    if is_generic_team_name(db_name):
        return inferred_name or fallback
    return db_name or inferred_name or fallback


def players_from_local_json():
    players = []
    for path in glob.glob(os.path.join(ROOT, "data", "sofascore_player_*")):
        player_id = os.path.basename(path).replace("sofascore_player_", "")
        stats_raw = read_json(path, "statistics.json") or {}
        player = stats_raw.get("player", {})
        name = player.get("name") or player.get("shortName") or f"Jogador {player_id}"
        players.append({"id": str(player_id), "name": name})
    return players


def dedupe_players(players):
    unique = {}
    for player in players:
        player_id = str(player.get("id"))
        if not player_id or player_id == "None":
            continue
        unique[player_id] = {
            "id": player_id,
            "name": player.get("name") or f"Jogador {player_id}",
        }
    return sorted(unique.values(), key=lambda x: x["name"] or "")


def stats_from_json(player_id, match_id):
    player_dir = data_dir_player(player_id)
    match_dir = data_dir_match(match_id)
    stats_raw = first_json(
        os.path.join(player_dir, "statistics.json"),
        os.path.join(match_dir, f"player_{player_id}_stats.json"),
    ) or {}
    stats_data = stats_raw.get("statistics", stats_raw)

    def g(key, default=0):
        return stats_data.get(key, default)

    return {
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
        "totalContest": g("totalContest"),
        "wonContest": g("wonContest"),
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
        "dribbleValueNormalized": g("dribbleValueNormalized"),
        "ballCarriesCount": g("ballCarriesCount"),
        "progressiveBallCarriesCount": g("progressiveBallCarriesCount"),
        "totalBallCarriesDistance": g("totalBallCarriesDistance"),
    }


def stats_from_db_row(stats_row):
    return {
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
        "totalContest": stats_row.get("total_contest", 0),
        "wonContest": stats_row.get("won_contest", 0),
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
    }


def has_stats_values(stats):
    return any(value not in (None, "", 0, 0.0) for value in stats.values())


def merge_stats(primary, fallback):
    merged = dict(primary or {})
    for key, value in (fallback or {}).items():
        if value in (None, ""):
            continue
        if merged.get(key) in (None, "", 0, 0.0):
            merged[key] = value
    return merged


def resolve_stats(player_id, match_id, stats_row=None):
    json_stats = stats_from_json(player_id, match_id)
    if stats_row:
        db_stats = stats_from_db_row(stats_row)
        return merge_stats(db_stats, json_stats), "database+json" if has_stats_values(json_stats) else "database"
    return json_stats, "json" if has_stats_values(json_stats) else "empty"


def to_events(raw_list):
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


def visual_payload_for_player(player_id, match_id):
    match_id_int = int(match_id)
    player_dir = data_dir_player(player_id)
    match_dir = data_dir_match(match_id)

    heatmap = (read_json(player_dir, "heatmap.json") or {}).get("heatmap", [])
    if not heatmap:
        heatmap = db.get_heatmap(match_id_int, player_id)

    shotmap = (read_json(player_dir, "shotmap.json") or {}).get("shotmap", [])
    if not shotmap:
        match_shotmap = read_json(match_dir, f"player_{player_id}_shotmap.json") or {}
        shotmap = match_shotmap.get("shotmap", [])
    if not shotmap:
        shotmap = format_shotmap(db.get_shotmap(match_id_int, player_id))

    rating_data = first_json(
        os.path.join(player_dir, "rating_breakdown.json"),
        os.path.join(match_dir, f"player_{player_id}_rating.json"),
        os.path.join(match_dir, f"player_{player_id}_events.json"),
    ) or {}
    events_file = read_json(match_dir, f"player_{player_id}_events.json") or {}
    passes = rating_data.get("passes", []) or events_file.get("passes", [])
    dribbles = rating_data.get("dribbles", []) or events_file.get("dribbles", [])
    defensive = rating_data.get("defensive", []) or events_file.get("defensive", [])
    ball_carries = (
        rating_data.get("ball-carries", [])
        or rating_data.get("ball_carry", [])
        or rating_data.get("ball_carries", [])
        or events_file.get("ball-carries", [])
        or events_file.get("ball_carry", [])
        or events_file.get("ball_carries", [])
    )

    if not passes:
        passes = to_events(db.get_player_events(match_id_int, player_id, "pass"))
    if not dribbles:
        dribbles = to_events(db.get_player_events(match_id_int, player_id, "dribble"))
    if not defensive:
        defensive = to_events(db.get_player_events(match_id_int, player_id, "defensive"))
    if not ball_carries:
        ball_carries = to_events(db.get_player_events(match_id_int, player_id, "ball_carry"))

    return {
        "heatmap": heatmap,
        "shotmap": shotmap,
        "events": {
            "pass": passes,
            "dribble": dribbles,
            "defensive": defensive,
            "ball_carry": ball_carries,
        },
    }


def aggregate_visual_payload(player_ids, match_id):
    events = {"pass": [], "dribble": [], "defensive": [], "ball_carry": []}

    for player_id in player_ids:
        payload = visual_payload_for_player(player_id, match_id)
        for event_type in events:
            events[event_type].extend(payload["events"].get(event_type, []))

    return {
        "events": {
            "pass": events["pass"][:100],
            "dribble": events["dribble"][:50],
            "defensive": events["defensive"][:50],
            "ball_carry": events["ball_carry"][:50],
        },
    }


def player_visual_images(player_id, match_id):
    payload = visual_payload_for_player(player_id, match_id)
    return {
        "heatmap": plot_heatmap(payload["heatmap"]),
        "shotmap": plot_shotmap(payload["shotmap"]),
        "passmap": plot_passmap(payload["events"]["pass"]),
    }


# ── API ──────────────────────────────────────────────────
@router.get("/api/players")
def get_players(match_id: str = MATCH_ID):
    """Retorna lista de jogadores (primeiro tenta banco, fallback JSON)."""
    match_id = normalize_match_id(match_id)
    cache_key = ("players", match_id)
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    match_players = db.get_match_players(int(match_id))
    if match_players:
        return set_cache(cache_key, {
            "players": [{"id": str(p["player_id"]), "name": p["name"]}
                        for p in match_players],
            "match_id": match_id,
            "source": "database",
        })

    db_players = db.list_players(200) if match_id == MATCH_ID else []
    if db_players:
        return set_cache(cache_key, {
            "players": [{"id": str(p["player_id"]), "name": p["name"]}
                        for p in db_players],
            "match_id": match_id,
            "source": "database",
        })

    players = dedupe_players(players_from_lineups(match_id) + players_from_local_json())
    source = "lineups" if players_from_lineups(match_id) else "local-json"
    if not players:
        source = "empty"
    return set_cache(cache_key, {"players": players, "match_id": match_id, "source": source})


@router.get("/api/dashboard-data")
def get_dashboard_data(player_id: str = "866469", match_id: str = MATCH_ID):
    match_id = normalize_match_id(match_id)
    cache_key = ("dashboard-data", match_id, player_id)
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    match_id_int = int(match_id)

    # ── 1. Tenta banco de dados (cache) ──
    stats_row = db.get_player_statistics(match_id_int, player_id)
    heatmap_pts = db.get_heatmap(match_id_int, player_id)
    shotmap_pts = db.get_shotmap(match_id_int, player_id)
    events_pass = db.get_player_events(match_id_int, player_id, "pass")
    events_dribble = db.get_player_events(match_id_int, player_id, "dribble")
    events_defensive = db.get_player_events(match_id_int, player_id, "defensive")
    events_carry = db.get_player_events(match_id_int, player_id, "ball_carry")

    has_maps = bool(heatmap_pts or shotmap_pts or events_pass)
    if stats_row and has_maps:
        stats_out, source = resolve_stats(player_id, match_id, stats_row)
        return set_cache(cache_key, _build_response(
            stats_row, heatmap_pts, shotmap_pts,
            events_pass, events_dribble, events_defensive, events_carry,
            match_id=match_id,
            player_id=player_id,
            source=source,
            stats_override=stats_out,
        ))

    # ── 2. Fallback: JSON files ──
    player_dir = data_dir_player(player_id)
    match_dir = data_dir_match(match_id)

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
    stats_out, stats_source = resolve_stats(player_id, match_id, stats_row)

    # Events
    rating_data = first_json(
        os.path.join(player_dir, "rating_breakdown.json"),
        os.path.join(match_dir, f"player_{player_id}_rating.json"),
        os.path.join(match_dir, f"player_{player_id}_events.json"),
    ) or {}
    rating_passes = rating_data.get("passes", [])
    if not rating_passes:
        events_file = read_json(match_dir, f"player_{player_id}_events.json") or {}
        rating_passes = events_file.get("passes", [])
    dribbles = rating_data.get("dribbles", []) or []
    defensive = rating_data.get("defensive", []) or []
    ball_carries = (
        rating_data.get("ball-carries", [])
        or rating_data.get("ball_carry", [])
        or rating_data.get("ball_carries", [])
    )

    # ── Gera imagens ──
    heatmap_b64 = plot_heatmap(hm_raw)
    shotmap_b64 = plot_shotmap(sm_raw)
    passmap_b64 = plot_passmap(rating_passes)

    source = stats_source if any([
        hm_raw, sm_raw, has_stats_values(stats_out),
        rating_passes, dribbles, defensive, ball_carries
    ]) else "empty"
    return set_cache(cache_key, {
        "match_id": match_id,
        "player_id": str(player_id),
        "images": {
            "heatmap": heatmap_b64,
            "shotmap": shotmap_b64,
            "passmap": passmap_b64,
        },
        "stats": stats_out,
        "events": {
            "pass": rating_passes[:50],
            "dribble": dribbles[:20],
            "defensive": defensive[:20],
            "ball_carry": ball_carries[:20],
        },
        "source": source,
    })


def _build_response(stats_row, heatmap_pts, shotmap_pts,
                    events_pass, events_dribble,
                    events_defensive, events_carry,
                    match_id=None,
                    player_id=None,
                    source="database",
                    stats_override=None):
    """Constrói resposta a partir de dados do banco."""
    heatmap_b64 = plot_heatmap(heatmap_pts)
    shotmap_b64 = plot_shotmap(format_shotmap(shotmap_pts))
    passmap_b64 = plot_passmap(to_events(events_pass))

    return {
        "match_id": normalize_match_id(match_id),
        "player_id": str(player_id) if player_id is not None else None,
        "images": {
            "heatmap": heatmap_b64,
            "shotmap": shotmap_b64,
            "passmap": passmap_b64,
        },
        "stats": stats_override or stats_from_db_row(stats_row),
        "events": {
            "pass": to_events(events_pass)[:50],
            "dribble": to_events(events_dribble)[:20],
            "defensive": to_events(events_defensive)[:20],
            "ball_carry": to_events(events_carry)[:20],
        },
        "source": source,
    }


@router.get("/api/matches")
def list_matches():
    cache_key = ("matches",)
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    db_matches = {str(m["match_id"]): m for m in db.list_matches(200)}
    matches = []
    for match_id in list_local_match_ids():
        lineups = read_lineups(match_id) or {}
        home = lineups.get("home", {})
        away = lineups.get("away", {})
        db_match = db_matches.get(str(match_id), {})
        matches.append({
            "match_id": int(match_id),
            "home_team": resolve_match_team_name(db_match.get("home_team"), home, "Home"),
            "away_team": resolve_match_team_name(db_match.get("away_team"), away, "Away"),
            "match_date": db_match.get("match_date"),
            "competition": db_match.get("competition"),
        })
    return set_cache(cache_key, {"matches": matches})


@router.get("/api/players/db")
def list_players_db():
    return {"players": db.list_players(200)}


@router.get("/api/compare")
def compare_players(player_ids: str, match_id: str = MATCH_ID):
    match_id = normalize_match_id(match_id)
    cache_key = ("compare", match_id, player_ids)
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    known_players = {p["id"]: p["name"] for p in get_players(match_id)["players"]}
    requested_ids = [p.strip() for p in player_ids.split(",") if p.strip()]
    result = []
    for player_id in requested_ids:
        stats_row = db.get_player_statistics(int(match_id), player_id)
        stats, source = resolve_stats(player_id, match_id, stats_row)
        player_name = known_players.get(player_id, f"Jogador {player_id}")
        result.append({
            "id": player_id,
            "name": player_name,
            "stats": stats,
            "source": source,
        })

    visual_payload = aggregate_visual_payload(requested_ids, match_id)
    visuals = [
        {
            "id": player["id"],
            "name": player["name"],
            "images": player_visual_images(player["id"], match_id),
        }
        for player in result
    ]
    return set_cache(cache_key, {
        "match_id": match_id,
        "players": result,
        "visuals": visuals,
        "events": visual_payload["events"],
        "source": "comparison",
    })
