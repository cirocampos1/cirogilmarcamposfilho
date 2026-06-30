import json
import os
import glob
from copy import deepcopy
from time import monotonic
from functools import lru_cache
from fastapi import APIRouter, HTTPException
from app.services.plotter import plot_heatmap, plot_shotmap, plot_passmap, plot_team_shotmap
from app.infra.database import DatabaseService

router = APIRouter()

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
db = DatabaseService()
CACHE_TTL_SECONDS = 60
_cache = {}


# ── Helpers ──────────────────────────────────────────────
def data_dir_player(player_id):
    return os.path.join(ROOT, "data", f"sofascore_player_{player_id}")

def data_dir_match(match_id):
    return os.path.join(ROOT, "data", "raw", f"match_{match_id}")

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
        del _cache[key]
        return None
    return deepcopy(item["value"])

def set_cache(key, value):
    _cache[key] = {"created_at": monotonic(), "value": deepcopy(value)}
    return value

def read_lineups(match_id):
    path = os.path.join(data_dir_match(match_id), "lineups.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    legacy = os.path.join(ROOT, "data", "sofascore", "lineups.json")
    if os.path.exists(legacy):
        with open(legacy, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def players_from_lineups(match_id):
    data = read_lineups(match_id) or {}
    players = []
    for team in ("home", "away"):
        for item in data.get(team, {}).get("players", []):
            p = item.get("player", {})
            if p.get("id") is not None:
                players.append({
                    "id": str(p["id"]),
                    "name": p.get("name", ""),
                    "position": p.get("position", ""),
                    "team": team,
                })
    return players

def team_name_from_lineup_side(side):
    direct = side.get("name") or (side.get("team", {}) or {}).get("name")
    if direct:
        return direct
    names = {}
    for item in side.get("players", []):
        player = item.get("player", {})
        country = (player.get("country", {}) or {}).get("name")
        if country:
            names[country] = names.get(country, 0) + 1
    if not names:
        return None
    return max(names.items(), key=lambda x: x[1])[0]

def dedupe_players(players):
    seen = {}
    for p in players:
        pid = str(p.get("id"))
        if not pid or pid == "None":
            continue
        seen[pid] = {"id": pid, "name": p.get("name", f"Jogador {pid}"), "position": p.get("position", ""), "team": p.get("team", "")}
    return sorted(seen.values(), key=lambda x: x["name"])


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
        "totalContest": g("totalContest"),
        "wonContest": g("wonContest"),
        "dribbleValueNormalized": g("dribbleValueNormalized"),
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

def resolve_stats(player_id, match_id, stats_row=None):
    json_stats = stats_from_json(player_id, match_id)
    if stats_row:
        db_stats = stats_from_db_row(stats_row)
        merged = dict(db_stats)
        for k, v in json_stats.items():
            if v not in (None, "", 0, 0.0) and merged.get(k) in (None, "", 0, 0.0):
                merged[k] = v
        return merged
    return json_stats

def to_events(raw_list):
    return [
        {
            "playerCoordinates": {"x": e["x"], "y": e["y"]},
            "passEndCoordinates": {"x": e.get("end_x", 0), "y": e.get("end_y", 0)},
            "outcome": bool(e["outcome"]),
            "keypass": bool(e["keypass"]),
            "isHome": bool(e.get("is_home", False)),
        }
        for e in raw_list if e.get("x") is not None
    ]

def format_shotmap(raw_shots):
    return [
        {
            "playerCoordinates": {"x": s["x"], "y": s["y"]},
            "shotType": s.get("shotType", "shot"),
        }
        for s in raw_shots if s.get("x") is not None
    ]


# ── API ──────────────────────────────────────────────────
@router.get("/api/players")
def get_players(match_id: int = None):
    try:
        if match_id is None:
            match_id = 15186850
        match_id_str = str(match_id)
        cache_key = ("players", match_id_str)
        cached = get_cache(cache_key)
        if cached is not None:
            return cached

        db_players = db.get_match_players(match_id)
        if db_players:
            players = [{"id": str(p["player_id"]), "name": p["name"]} for p in db_players]
            return set_cache(cache_key, {"players": sorted(players, key=lambda x: x["name"] or "")})

        return {"players": []}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar jogadores: {str(e)}")


@router.get("/api/dashboard-data")
def get_dashboard_data(player_id: str = "866469", match_id: int = None):
    if match_id is None:
        match_id = 15186850
    cache_key = ("dashboard-data", str(match_id), player_id)
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    try:
        stats_row = db.get_player_statistics(match_id, player_id)
        heatmap_pts = db.get_heatmap(match_id, player_id)
        shotmap_pts = db.get_shotmap(match_id, player_id)
        events_pass = db.get_player_events(match_id, player_id, "pass")
        events_dribble = db.get_player_events(match_id, player_id, "dribble")
        events_defensive = db.get_player_events(match_id, player_id, "defensive")
        events_carry = db.get_player_events(match_id, player_id, "ball_carry")

        has_maps = bool(heatmap_pts or shotmap_pts or events_pass)
        if stats_row and has_maps:
            stats = resolve_stats(player_id, match_id, stats_row)
            return set_cache(cache_key, _build_response(
                stats, heatmap_pts, shotmap_pts,
                events_pass, events_dribble, events_defensive, events_carry,
            ))

        player_dir = data_dir_player(player_id)
        match_dir = data_dir_match(match_id)

        hm_raw = (read_json(player_dir, "heatmap.json") or {}).get("heatmap", [])
        if not hm_raw:
            hm_raw = heatmap_pts or []

        sm_raw = (read_json(player_dir, "shotmap.json") or {}).get("shotmap", [])
        if not sm_raw:
            sm2 = read_json(match_dir, f"player_{player_id}_shotmap.json")
            if sm2:
                sm_raw = sm2.get("shotmap", [])

        stats = resolve_stats(player_id, match_id, stats_row)

        rating_data = first_json(
            os.path.join(player_dir, "rating_breakdown.json"),
            os.path.join(match_dir, f"player_{player_id}_rating.json"),
            os.path.join(match_dir, f"player_{player_id}_events.json"),
        ) or {}
        passes = rating_data.get("passes", [])
        if not passes:
            evt = read_json(match_dir, f"player_{player_id}_events.json") or {}
            passes = evt.get("passes", [])

        heatmap_b64 = plot_heatmap(hm_raw)
        shotmap_b64 = plot_shotmap(sm_raw)
        passmap_b64 = plot_passmap(passes)

        return set_cache(cache_key, {
            "images": {"heatmap": heatmap_b64, "shotmap": shotmap_b64, "passmap": passmap_b64},
            "stats": stats,
            "events": {
                "pass": passes[:50],
                "dribble": (rating_data.get("dribbles", []) or [])[:20],
                "defensive": (rating_data.get("defensive", []) or [])[:20],
                "ball_carry": (rating_data.get("ball-carries", []) or rating_data.get("ball_carry", []) or [])[:20],
            },
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no dashboard: {str(e)}")


def _build_response(stats_out, heatmap_pts, shotmap_pts,
                    events_pass, events_dribble,
                    events_defensive, events_carry):
    heatmap_b64 = plot_heatmap(heatmap_pts)
    shotmap_b64 = plot_shotmap(format_shotmap(shotmap_pts) if shotmap_pts else [])
    passmap_b64 = plot_passmap(to_events(events_pass) if events_pass else [])

    return {
        "images": {"heatmap": heatmap_b64, "shotmap": shotmap_b64, "passmap": passmap_b64},
        "stats": stats_out,
        "events": {
            "pass": to_events(events_pass)[:50] if events_pass else [],
            "dribble": to_events(events_dribble)[:20] if events_dribble else [],
            "defensive": to_events(events_defensive)[:20] if events_defensive else [],
            "ball_carry": to_events(events_carry)[:20] if events_carry else [],
        },
    }


# ── Compare ──────────────────────────────────────────────
@router.get("/api/compare")
def compare_players(player_ids: str, match_id: int = None):
    if match_id is None:
        match_id = 15186850
    match_id_str = str(match_id)
    cache_key = ("compare", match_id_str, player_ids)
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    requested = [p.strip() for p in player_ids.split(",") if p.strip()]
    result = []
    all_heatmap = []
    all_shotmap = []
    all_events = {"pass": [], "dribble": [], "defensive": [], "ball_carry": []}

    for pid in requested:
        stats_row = db.get_player_statistics(match_id, pid)
        stats = resolve_stats(pid, match_id, stats_row)

        player_dir = data_dir_player(pid)
        match_dir = data_dir_match(match_id)

        hm = (read_json(player_dir, "heatmap.json") or {}).get("heatmap", []) or db.get_heatmap(match_id, pid) or []
        sm = (read_json(player_dir, "shotmap.json") or {}).get("shotmap", [])
        if not sm:
            sm2 = read_json(match_dir, f"player_{pid}_shotmap.json") or {}
            sm = sm2.get("shotmap", []) or db.get_shotmap(match_id, pid) or []

        all_heatmap.extend(hm)
        all_shotmap.extend(sm)

        rating_data = first_json(
            os.path.join(player_dir, "rating_breakdown.json"),
            os.path.join(match_dir, f"player_{pid}_rating.json"),
        ) or {}
        for etype in all_events:
            data = rating_data.get(etype, []) or rating_data.get(etype.replace("_", "-"), [])
            if not data and etype == "pass":
                evt = read_json(match_dir, f"player_{pid}_events.json") or {}
                data = evt.get("passes", [])
            all_events[etype].extend(data[:30])

        heatmap_b64 = plot_heatmap(hm)
        shotmap_b64 = plot_shotmap(sm)
        passmap_b64 = plot_passmap(rating_data.get("passes", []))

        result.append({
            "id": str(pid),
            "stats": stats,
            "images": {"heatmap": heatmap_b64, "shotmap": shotmap_b64, "passmap": passmap_b64},
        })

    return set_cache(cache_key, {
        "players": result,
        "events": {k: v[:60] for k, v in all_events.items()},
    })


# ── Match Moments ────────────────────────────────────────
@router.get("/api/match-moments")
def match_moments(match_id: int = None):
    if match_id is None:
        match_id = 15186850
    cache_key = ("moments", str(match_id))
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    incidents = first_json(
        os.path.join(data_dir_match(match_id), "incidents.json"),
        os.path.join(ROOT, "data", "sofascore", "incidents.json"),
    )
    if not incidents:
        return set_cache(cache_key, {"moments": []})

    raw_list = incidents.get("incidents", [])
    moments = []
    for inc in raw_list:
        itype = inc.get("incidentType", "")
        minute = inc.get("time", 0)
        added = inc.get("addedTime", 0)

        if itype in ("period", "injuryTime"):
            continue

        moment = {
            "type": itype,
            "minute": minute,
            "addedTime": added,
            "isHome": inc.get("isHome", True),
            "text": inc.get("text", ""),
        }

        if itype == "goal":
            player = inc.get("player", {})
            moment["playerName"] = player.get("name", player.get("shortName", ""))
            moment["playerId"] = player.get("id")
            assist = inc.get("assist1", {})
            moment["assist"] = assist.get("name", assist.get("shortName", ""))
            moment["homeScore"] = inc.get("homeScore")
            moment["awayScore"] = inc.get("awayScore")
            moment["bodyPart"] = inc.get("bodyPart", "")

        elif itype == "card":
            player = inc.get("player", {})
            moment["playerName"] = player.get("name", player.get("shortName", ""))
            moment["playerId"] = player.get("id")
            moment["cardType"] = inc.get("cardType", "yellow")
            moment["reason"] = inc.get("reason", "")

        elif itype == "substitution":
            pin = inc.get("playerIn", {})
            pout = inc.get("playerOut", {})
            moment["playerIn"] = pin.get("name", pin.get("shortName", ""))
            moment["playerOut"] = pout.get("name", pout.get("shortName", ""))

        elif itype == "var":
            moment["decision"] = inc.get("decision", "")
            moment["reason"] = inc.get("reason", "")

        elif itype == "penalty":
            player = inc.get("player", {})
            moment["playerName"] = player.get("name", "")
            moment["scored"] = inc.get("scored", False)
            moment["homeScore"] = inc.get("homeScore")
            moment["awayScore"] = inc.get("awayScore")

        moments.append(moment)

    moments.sort(key=lambda m: (m["minute"], m.get("addedTime", 0)))
    return set_cache(cache_key, {"moments": moments})


# ── Players by Position ──────────────────────────────────
@router.get("/api/players-by-position")
def players_by_position(match_id: int = None, team: str = None, position: str = None):
    if match_id is None:
        match_id = 15186850
    match_id_str = str(match_id)
    cache_key = ("players-by-position", match_id_str, team or "all", position or "all")
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    all_players = players_from_lineups(match_id)
    if not all_players:
        match_players = db.get_match_players(match_id)
        for mp in match_players:
            all_players.append({
                "id": str(mp["player_id"]),
                "name": mp["name"],
                "position": mp.get("position", ""),
                "team": mp.get("team_side", ""),
            })

    filtered = all_players
    if team and team != "all":
        filtered = [p for p in filtered if p["team"] == team]
    if position and position != "all":
        filtered = [p for p in filtered if p["position"] and p["position"][0].upper() == position[0].upper()]

    return set_cache(cache_key, {
        "players": dedupe_players(filtered),
        "match_id": match_id_str,
    })


# ── Team Shotmap ─────────────────────────────────────────
@router.get("/api/team-shotmap")
def team_shotmap(match_id: int = None, team: str = None):
    if match_id is None:
        match_id = 15186850
    cache_key = ("team-shotmap", str(match_id), team or "all")
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    match_dir = data_dir_match(match_id)
    all_shots = []
    home_name = "Home"
    away_name = "Away"

    raw_lineups = read_lineups(match_id)
    if raw_lineups:
        home_name = raw_lineups.get("home", {}).get("name", "Home") or "Home"
        away_name = raw_lineups.get("away", {}).get("name", "Away") or "Away"

    # Collect all shots from player shotmap files
    for sp in glob.glob(os.path.join(match_dir, "*_shotmap.json")):
        with open(sp, "r", encoding="utf-8") as f:
            data = json.load(f)
        shots = data.get("shotmap", [])
        all_shots.extend(shots)

    # Also try DB
    if not all_shots:
        all_shots = db.get_shotmap(match_id, None) or []
        if all_shots:
            all_shots = [{"x": s["x"], "y": s["y"], "shotType": s.get("shotType", "shot"),
                          "playerId": s.get("player_id", "")} for s in all_shots if s.get("x")]

    if not all_shots:
        return set_cache(cache_key, {"shots": [], "image": None, "homeName": home_name, "awayName": away_name})

    # If team filter, we need player team info
    if team:
        team_players = {p["id"] for p in players_from_lineups(match_id) if p["team"] == team}
        all_shots = [s for s in all_shots if str(s.get("playerId", s.get("player_id", ""))) in team_players]

    image = plot_team_shotmap(all_shots)

    home_shots = sum(1 for s in all_shots if s.get("isHome", True))
    away_shots = len(all_shots) - home_shots
    goals = [s for s in all_shots if s.get("shotType") == "goal"]
    on_target = [s for s in all_shots if s.get("shotType") in ("shot", "shotOnTarget")]

    return set_cache(cache_key, {
        "shots": all_shots,
        "image": image,
        "stats": {
            "total": len(all_shots),
            "goals": len(goals),
            "onTarget": len(on_target),
            "homeShots": home_shots,
            "awayShots": away_shots,
        },
        "homeName": home_name,
        "awayName": away_name,
    })


# ── Existing ──────────────────────────────────────────────
@router.get("/api/players/db")
def list_players_db():
    return {"players": db.list_players(200)}

@router.get("/api/matches")
def list_matches():
    cache_key = ("matches",)
    cached = get_cache(cache_key)
    if cached is not None:
        return cached

    db_matches = db.list_matches(50)
    matches = []
    for m in db_matches:
        lineups = read_lineups(str(m["match_id"]))
        side = lineups.get("home", {}) if lineups else {}
        home = team_name_from_lineup_side(side) or m.get("home_team", "Home")
        side = lineups.get("away", {}) if lineups else {}
        away = team_name_from_lineup_side(side) or m.get("away_team", "Away")
        matches.append({
            "match_id": m["match_id"],
            "home_team": home,
            "away_team": away,
            "match_date": m.get("match_date", ""),
            "competition": m.get("competition", ""),
        })
    return set_cache(cache_key, {"matches": matches})
