import os
import json
import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

TEAM_TRANSLATIONS = {
    "Argentina": "Argentina",
    "Australia": "Austrália",
    "Belgium": "Bélgica",
    "Brazil": "Brasil",
    "Cameroon": "Camarões",
    "Canada": "Canadá",
    "Costa Rica": "Costa Rica",
    "Croatia": "Croácia",
    "Denmark": "Dinamarca",
    "Ecuador": "Equador",
    "England": "Inglaterra",
    "France": "França",
    "Germany": "Alemanha",
    "Ghana": "Gana",
    "Iran": "Irã",
    "Japan": "Japão",
    "Mexico": "México",
    "Morocco": "Marrocos",
    "Netherlands": "Holanda",
    "Poland": "Polônia",
    "Portugal": "Portugal",
    "Qatar": "Catar",
    "Saudi Arabia": "Arábia Saudita",
    "Senegal": "Senegal",
    "Serbia": "Sérvia",
    "South Korea": "Coreia do Sul",
    "Spain": "Espanha",
    "Switzerland": "Suíça",
    "Tunisia": "Tunísia",
    "United States": "Estados Unidos",
    "Uruguay": "Uruguai",
    "Wales": "País de Gales"
}

def translate_team(name):
    if not name:
        return name
    return TEAM_TRANSLATIONS.get(name, name)


STAGE_TRANSLATIONS = {
    "Group Stage": "Fase de Grupos",
    "Round of 16": "Oitavas de Final",
    "Quarter-finals": "Quartas de Final",
    "Semi-finals": "Semifinais",
    "3rd Place Final": "Disputa do 3º Lugar",
    "Final": "Final"
}

def translate_stage(stage):
    if not stage:
        return stage
    return STAGE_TRANSLATIONS.get(stage, stage)


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
        # Filter matches that actually have data folders in data/raw
        filtered_data = []
        for m in data:
            match_id = m.get("match_id")
            if match_id and os.path.exists(os.path.join(DATA_DIR, f"match_{match_id}")):
                filtered_data.append(m)
        return replace_nan(filtered_data)

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


def clean_id(val):
    if val is None:
        return ""
    try:
        # Convert float-like string (e.g., '2954.0') to integer string ('2954')
        return str(int(float(val)))
    except (ValueError, TypeError):
        return str(val)


def get_player_stats_for_match(match_id):
    events = get_match_events(match_id)
    if not events:
        return {}
    
    # Build a pass dict to lookup by id for xA calculation
    pass_dict = {}
    for e in events:
        if e.get("type") == "Pass":
            pass_id = e.get("id")
            if pass_id:
                pass_dict[pass_id] = e
            
    # Initialize stats dict
    stats = {}
    
    # Parse events to compute player stats
    for e in events:
        player_info = e.get("player")
        if not player_info:
            continue
        
        # Get player ID and name
        if isinstance(player_info, dict):
            pid = player_info.get("id")
            pname = player_info.get("name")
        else:
            pid = e.get("player_id")
            pname = player_info
            
        if not pid:
            continue
            
        pid = clean_id(pid)
        if pid not in stats:
            team_val = e.get("team")
            team_name = team_val.get("name") if isinstance(team_val, dict) else team_val
            stats[pid] = {
                "player_id": pid,
                "name": pname,
                "team": team_name,
                "goals": 0,
                "assists": 0,
                "xg": 0.0,
                "xa": 0.0,
                "shots": 0,
                "shots_on_target": 0,
                "passes_total": 0,
                "passes_completed": 0,
                "passes_progressive": 0,
                "passes_under_pressure_total": 0,
                "passes_under_pressure_completed": 0,
                "dribbles_total": 0,
                "dribbles_completed": 0,
                "defensive_actions": 0,
                "counterpress_actions": 0,
                "tackles_total": 0,
                "tackles_won": 0,
                "interceptions": 0,
                "blocks": 0,
                "clearances": 0
            }
            
        p_stats = stats[pid]
        etype = e.get("type")
        
        # Goals and xG
        if etype == "Shot":
            p_stats["shots"] += 1
            xg = e.get("shot_statsbomb_xg", 0.0) or 0.0
            p_stats["xg"] += xg
            outcome = e.get("shot_outcome")
            if outcome == "Goal":
                p_stats["goals"] += 1
            if outcome in ["Goal", "Saved"]:
                p_stats["shots_on_target"] += 1
                
            # xA (Expected Assists) - check shot's key pass ID
            key_pass_id = e.get("shot_key_pass_id")
            if key_pass_id and key_pass_id in pass_dict:
                pass_event = pass_dict[key_pass_id]
                passer_info = pass_event.get("player")
                if passer_info:
                    raw_passer_id = passer_info.get("id") if isinstance(passer_info, dict) else pass_event.get("player_id")
                    passer_id = clean_id(raw_passer_id)
                    # Make sure passer exists in stats
                    if passer_id not in stats:
                        passer_team_val = pass_event.get("team")
                        passer_team_name = passer_team_val.get("name") if isinstance(passer_team_val, dict) else passer_team_val
                        stats[passer_id] = {
                            "player_id": passer_id,
                            "name": passer_info.get("name") if isinstance(passer_info, dict) else passer_info,
                            "team": passer_team_name,
                            "goals": 0,
                            "assists": 0,

                            "xg": 0.0,
                            "xa": 0.0,
                            "shots": 0,
                            "shots_on_target": 0,
                            "passes_total": 0,
                            "passes_completed": 0,
                            "passes_progressive": 0,
                            "passes_under_pressure_total": 0,
                            "passes_under_pressure_completed": 0,
                            "dribbles_total": 0,
                            "dribbles_completed": 0,
                            "defensive_actions": 0,
                            "counterpress_actions": 0,
                            "tackles_total": 0,
                            "tackles_won": 0,
                            "interceptions": 0,
                            "blocks": 0,
                            "clearances": 0
                        }
                    stats[passer_id]["xa"] += xg
                    if outcome == "Goal":
                        stats[passer_id]["assists"] += 1
                            
        # Passes
        elif etype == "Pass":
            p_stats["passes_total"] += 1
            outcome = e.get("pass_outcome")
            is_completed = not outcome
            if is_completed:
                p_stats["passes_completed"] += 1
                
                # Progressive Pass Check (x2 - x1 >= 10)
                loc = e.get("location")
                end_loc = e.get("pass_end_location")
                if loc and end_loc:
                    x1, x2 = loc[0], end_loc[0]
                    if (x2 - x1) >= 10:
                        p_stats["passes_progressive"] += 1
            
            # Passes under pressure
            if e.get("under_pressure"):
                p_stats["passes_under_pressure_total"] += 1
                if is_completed:
                    p_stats["passes_under_pressure_completed"] += 1
                    
        # Dribbles
        elif etype == "Dribble":
            p_stats["dribbles_total"] += 1
            outcome = e.get("dribble_outcome")
            if outcome == "Complete":
                p_stats["dribbles_completed"] += 1
                
        # Defensive Actions
        elif etype in ["Interception", "Duel", "Block", "Clearance", "Foul Committed"]:
            p_stats["defensive_actions"] += 1
            if e.get("counterpress"):
                p_stats["counterpress_actions"] += 1
                
            if etype == "Interception":
                p_stats["interceptions"] += 1
            elif etype == "Block":
                p_stats["blocks"] += 1
            elif etype == "Clearance":
                p_stats["clearances"] += 1
            elif etype == "Duel":
                dt = e.get("duel_type")
                if dt == "Tackle":
                    p_stats["tackles_total"] += 1
                    do = e.get("duel_outcome")
                    if do in ["Won", "Success In Play", "Success Out"]:
                        p_stats["tackles_won"] += 1
                        
    # Round floats
    for pid in stats:
        stats[pid]["xg"] = round(stats[pid]["xg"], 2)
        stats[pid]["xa"] = round(stats[pid]["xa"], 2)
        
    return stats

