import os
import json
import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

def replace_nan(obj):
    if isinstance(obj, float) and math.isnan(obj):
        return None
    elif isinstance(obj, dict):
        return {k: replace_nan(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_nan(i) for i in obj]
    return obj

def get_matches():
    matches_file = os.path.join(DATA_DIR, "matches.json")
    if not os.path.exists(matches_file):
        return []
    with open(matches_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return replace_nan(data)

def get_match_events(match_id):
    events_file = os.path.join(DATA_DIR, f"match_{match_id}", "events.json")
    if not os.path.exists(events_file):
        return []
    with open(events_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return replace_nan(data)

def get_match_lineups(match_id):
    lineups_file = os.path.join(DATA_DIR, f"match_{match_id}", "lineups.json")
    if not os.path.exists(lineups_file):
        return {}
    with open(lineups_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return replace_nan(data)

def extract_shots(events):
    shots = []
    for e in events:
        if e.get("type") == "Shot":
            shots.append(e)
    return shots

def extract_passes(events):
    passes = []
    for e in events:
        if e.get("type") == "Pass":
            passes.append(e)
    return passes

def extract_pressure_events(events):
    pressures = []
    for e in events:
        if e.get("type") == "Pressure":
            pressures.append(e)
    return pressures

def calculate_advanced_metrics(events, home_team, away_team):
    metrics = {
        "home": {"xg": 0.0, "goals": 0, "passes_under_pressure_total": 0, "passes_under_pressure_completed": 0, "high_turnovers": 0, "ppda": 0.0},
        "away": {"xg": 0.0, "goals": 0, "passes_under_pressure_total": 0, "passes_under_pressure_completed": 0, "high_turnovers": 0, "ppda": 0.0}
    }
    
    # PPDA counters
    home_passes_allowed = 0
    away_passes_allowed = 0
    home_def_actions = 0
    away_def_actions = 0
    
    for e in events:
        team_raw = e.get("possession_team") or e.get("team")
        team = team_raw.get("name") if isinstance(team_raw, dict) else team_raw
        
        t_key = "home" if team == home_team else "away" if team == away_team else None
        if not t_key: continue
        
        event_type = e.get("type")
        loc = e.get("location")
        
        # xG and Goals
        if event_type == "Shot":
            metrics[t_key]["xg"] += e.get("shot_statsbomb_xg", 0.0) or 0.0
            if e.get("shot_outcome") == "Goal":
                metrics[t_key]["goals"] += 1
                
        # Passes under pressure
        elif event_type == "Pass":
            if e.get("under_pressure"):
                metrics[t_key]["passes_under_pressure_total"] += 1
                outcome = e.get("pass_outcome")
                if not outcome:
                    metrics[t_key]["passes_under_pressure_completed"] += 1
            
            # PPDA: passes do oponente permitidos na sua metade/terço inicial (x <= 80)
            if loc and isinstance(loc, list) and len(loc) >= 1 and loc[0] <= 80:
                if t_key == "home":
                    home_passes_allowed += 1
                else:
                    away_passes_allowed += 1
                    
        # High turnovers and other defensive actions
        if event_type in ["Interception", "Duel", "Block", "Ball Recovery", "Foul Committed", "Pressure"]:
            if event_type in ["Interception", "Duel", "Block", "Ball Recovery"]:
                if loc and isinstance(loc, list) and len(loc) >= 2 and loc[0] >= 80:
                    metrics[t_key]["high_turnovers"] += 1
            
            # PPDA: ações defensivas em campo de ataque (x >= 40)
            if loc and isinstance(loc, list) and len(loc) >= 1 and loc[0] >= 40:
                if t_key == "home":
                    home_def_actions += 1
                else:
                    away_def_actions += 1

    # Round xG
    metrics["home"]["xg"] = round(metrics["home"]["xg"], 2)
    metrics["away"]["xg"] = round(metrics["away"]["xg"], 2)
    
    # Calculate PPDA: passes do oponente na própria metade / ações defensivas do time na metade do oponente
    # Para o time da casa (home), o oponente é away_team. Então usamos away_passes_allowed / home_def_actions
    metrics["home"]["ppda"] = round(away_passes_allowed / home_def_actions, 1) if home_def_actions > 0 else 0.0
    metrics["away"]["ppda"] = round(home_passes_allowed / away_def_actions, 1) if away_def_actions > 0 else 0.0

    return metrics
def extract_xg_flow(shots, home_team, away_team):
    # Sort shots by minute
    sorted_shots = sorted(shots, key=lambda x: x.get('minute', 0))
    flow = {"home": {"minutes": [0], "xg": [0.0]}, "away": {"minutes": [0], "xg": [0.0]}}
    
    home_xg = 0.0
    away_xg = 0.0
    
    for s in sorted_shots:
        team_raw = s.get('possession_team') or s.get('team')
        team = team_raw.get("name") if isinstance(team_raw, dict) else team_raw
        
        minute = s.get('minute', 0)
        xg = s.get('shot_statsbomb_xg', 0.0) or 0.0
        
        if team == home_team:
            home_xg += xg
            flow["home"]["minutes"].append(minute)
            flow["home"]["xg"].append(round(home_xg, 2))
        elif team == away_team:
            away_xg += xg
            flow["away"]["minutes"].append(minute)
            flow["away"]["xg"].append(round(away_xg, 2))
            
    # Append final minute
    final_minute = max([s.get('minute', 90) for s in shots] + [90])
    flow["home"]["minutes"].append(final_minute)
    flow["home"]["xg"].append(round(home_xg, 2))
    flow["away"]["minutes"].append(final_minute)
    flow["away"]["xg"].append(round(away_xg, 2))
    
    return flow

def is_progressive_pass(x1, y1, x2, y2):
    # Gol adversário em (120, 40)
    dist_start = math.sqrt((120 - x1)**2 + (40 - y1)**2)
    dist_end = math.sqrt((120 - x2)**2 + (40 - y2)**2)
    
    diff = dist_start - dist_end
    
    if x1 < 60:
        return diff >= 30
    elif 60 <= x1 < 80:
        return diff >= 15
    else:
        return diff >= 10

def calculate_player_statistics(events):
    # Dicionário de xG de chutes mapeados por shot_key_pass_id
    key_pass_xg = {}
    for e in events:
        if e.get("type") == "Shot":
            kp_id = e.get("shot_key_pass_id")
            if kp_id:
                xg = e.get("shot_statsbomb_xg", 0.0) or 0.0
                key_pass_xg[kp_id] = xg

    player_stats = {}

    for e in events:
        player_obj = e.get("player")
        if not player_obj:
            continue
            
        if isinstance(player_obj, dict):
            player_id = player_obj.get("id")
            player_name = player_obj.get("name")
        else:
            player_id = player_obj
            player_name = player_obj
            
        if not player_id:
            continue

        team_obj = e.get("team")
        team_name = team_obj.get("name") if isinstance(team_obj, dict) else (team_obj or "Desconhecido")

        if player_id not in player_stats:
            player_stats[player_id] = {
                "player_id": player_id,
                "name": player_name,
                "team": team_name,
                "goals": 0,
                "xg": 0.0,
                "xa": 0.0,
                "passes_total": 0,
                "passes_completed": 0,
                "passes_under_pressure_total": 0,
                "passes_under_pressure_completed": 0,
                "progressive_passes": 0,
                "tackles": 0,
                "interceptions": 0,
                "recoveries": 0,
                "fouls_committed": 0,
                "dribbles_attempted": 0,
                "dribbles_completed": 0,
                "minutes_played": 90
            }

        stats = player_stats[player_id]
        event_type = e.get("type")

        # Goals & xG
        if event_type == "Shot":
            stats["xg"] += e.get("shot_statsbomb_xg", 0.0) or 0.0
            if e.get("shot_outcome") == "Goal":
                stats["goals"] += 1

        # Passes, xA, Progressive
        elif event_type == "Pass":
            stats["passes_total"] += 1
            
            # Outcome
            outcome = e.get("pass_outcome")
            is_complete = not outcome # None in pass_outcome means complete in Statsbomb
            
            if is_complete:
                stats["passes_completed"] += 1
                
                # Check Progressive
                loc = e.get("location")
                end_loc = e.get("pass_end_location")
                if loc and end_loc and isinstance(loc, list) and isinstance(end_loc, list) and len(loc) >= 2 and len(end_loc) >= 2:
                    if is_progressive_pass(loc[0], loc[1], end_loc[0], end_loc[1]):
                        stats["progressive_passes"] += 1
            
            # Under Pressure
            if e.get("under_pressure"):
                stats["passes_under_pressure_total"] += 1
                if is_complete:
                    stats["passes_under_pressure_completed"] += 1
                    
            # xA
            pass_uuid = e.get("id")
            if pass_uuid in key_pass_xg:
                stats["xa"] += key_pass_xg[pass_uuid]

        # Defensive stats
        elif event_type == "Duel":
            duel_type = e.get("duel_type")
            if duel_type == "Tackle":
                stats["tackles"] += 1
        elif event_type == "Interception":
            stats["interceptions"] += 1
        elif event_type == "Ball Recovery":
            stats["recoveries"] += 1
        elif event_type == "Foul Committed":
            stats["fouls_committed"] += 1
            
        # Dribbles
        elif event_type == "Dribble":
            stats["dribbles_attempted"] += 1
            d_outcome = e.get("dribble_outcome")
            if d_outcome == "Complete":
                stats["dribbles_completed"] += 1

    # Round floats
    for p_id, stats in player_stats.items():
        stats["xg"] = round(stats["xg"], 2)
        stats["xa"] = round(stats["xa"], 2)

    return player_stats
