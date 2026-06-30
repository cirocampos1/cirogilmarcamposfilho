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
        "home": {"xg": 0.0, "goals": 0, "passes_under_pressure_total": 0, "passes_under_pressure_completed": 0, "high_turnovers": 0},
        "away": {"xg": 0.0, "goals": 0, "passes_under_pressure_total": 0, "passes_under_pressure_completed": 0, "high_turnovers": 0}
    }
    
    for e in events:
        team_raw = e.get("possession_team") or e.get("team")
        team = team_raw.get("name") if isinstance(team_raw, dict) else team_raw
        
        t_key = "home" if team == home_team else "away" if team == away_team else None
        if not t_key: continue
        
        # xG and Goals
        if e.get("type") == "Shot":
            metrics[t_key]["xg"] += e.get("shot_statsbomb_xg", 0.0) or 0.0
            if e.get("shot_outcome") == "Goal":
                metrics[t_key]["goals"] += 1
                
        # Passes under pressure
        if e.get("type") == "Pass":
            # under_pressure can be True or 1.0
            if e.get("under_pressure"):
                metrics[t_key]["passes_under_pressure_total"] += 1
                # If pass has no outcome, it is considered complete
                outcome = e.get("pass_outcome")
                if not outcome:
                    metrics[t_key]["passes_under_pressure_completed"] += 1
                    
        # High turnovers (Interception, Duel, Block, Ball Recovery in attacking third leading to possession change? Actually, just count possession changes high up)
        if e.get("type") in ["Interception", "Duel", "Block", "Ball Recovery"]:
            loc = e.get("location")
            if loc and isinstance(loc, list) and len(loc) >= 2 and loc[0] >= 80:
                metrics[t_key]["high_turnovers"] += 1

    # Round xG
    metrics["home"]["xg"] = round(metrics["home"]["xg"], 2)
    metrics["away"]["xg"] = round(metrics["away"]["xg"], 2)

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
