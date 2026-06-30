from fastapi import APIRouter, HTTPException
from app.services import statsbomb_parser
from app.services import plotter

router = APIRouter()

@router.get("/api/matches")
def get_matches():
    matches = statsbomb_parser.get_matches()
    return {"matches": matches}

@router.get("/api/matches/{match_id}")
def get_match_detail(match_id: int):
    # Retrieve match events and lineups
    events = statsbomb_parser.get_match_events(match_id)
    lineups = statsbomb_parser.get_match_lineups(match_id)
    
    if not events:
        raise HTTPException(status_code=404, detail="Match data not found")
        
    shots = statsbomb_parser.extract_shots(events)
    passes = statsbomb_parser.extract_passes(events)
    pressures = statsbomb_parser.extract_pressure_events(events)
    
    matches = statsbomb_parser.get_matches()
    match_info = next((m for m in matches if m["match_id"] == match_id), {})
    home_team = match_info.get("home_team")
    away_team = match_info.get("away_team")
    
    adv_metrics = statsbomb_parser.calculate_advanced_metrics(events, home_team, away_team)
    xg_flow_data = statsbomb_parser.extract_xg_flow(shots, home_team, away_team)
    
    # Render maps
    shotmap_b64 = plotter.plot_jointgrid_shotmap(shots, lineups)
    passmap_b64 = plotter.plot_pass_network(passes, lineups)
    xg_flow_b64 = plotter.plot_xg_flow(xg_flow_data, home_team, away_team)
    pressure_heatmap_b64 = plotter.plot_pressure_heatmap(pressures, home_team, away_team)

    summary = {
        "total_shots": len(shots),
        "total_passes": len(passes),
        "competition_stage": match_info.get("competition_stage", ""),
        "stadium": f'{match_info.get("stadium", "")}, {match_info.get("stadium_country_name", "")}',
        "referee": match_info.get("referee", ""),
        "home_manager": match_info.get("home_managers", ""),
        "away_manager": match_info.get("away_managers", ""),
        "score": f'{match_info.get("home_score", 0)} - {match_info.get("away_score", 0)}',
        "date": match_info.get("match_date"),
        "kick_off": match_info.get("kick_off"),
        "advanced_metrics": adv_metrics
    }

    return {
        "match_id": match_id,
        "summary": summary,
        "images": {
            "shotmap": shotmap_b64,
            "pass_network": passmap_b64,
            "xg_flow": xg_flow_b64,
            "pressure_heatmap": pressure_heatmap_b64
        }
    }
