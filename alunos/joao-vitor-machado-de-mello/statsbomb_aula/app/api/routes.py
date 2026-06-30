from fastapi import APIRouter, HTTPException

from app.services import processed_data
from app.services import statsbomb_parser


router = APIRouter()


def _display_manifest_match(match):
    home = statsbomb_parser.get_team_display(match["home_team"])
    away = statsbomb_parser.get_team_display(match["away_team"])
    colors = statsbomb_parser.resolve_match_colors(home, away)
    return {
        **match,
        "home_team_raw": match["home_team"],
        "away_team_raw": match["away_team"],
        "home_team": home["name"],
        "away_team": away["name"],
        "home_flag": home["flag"],
        "away_flag": away["flag"],
        "home_flag_code": home["flag_code"],
        "away_flag_code": away["flag_code"],
        "home_flag_style": home["flag_style"],
        "away_flag_style": away["flag_style"],
        "home_flag_url": home["flag_url"],
        "away_flag_url": away["flag_url"],
        "home_primary_color": colors["home"],
        "away_primary_color": colors["away"],
        "competition_stage_raw": match["stage"],
        "competition_stage": statsbomb_parser.translate_stage(match["stage"]),
        "match_date": match["date"],
        "match_date_display": statsbomb_parser.format_match_date(match["date"]),
        "score": f"{match['home_score']} - {match['away_score']}",
        "display_label": match["display_name"],
        "sort_key": match["date"] or "",
    }


@router.get("/api/matches")
def get_matches():
    try:
        manifest = processed_data.load_manifest()
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=503,
            detail=(
                "Processed dashboard data is missing. "
                "Run python scripts/build_dashboard_data.py."
            ),
        ) from exc
    return {
        "matches": [
            _display_manifest_match(match)
            for match in manifest
        ]
    }


@router.get("/api/matches/{match_id}")
def get_match_detail(match_id: int):
    try:
        return processed_data.load_match_payload(match_id)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=(
                f"Processed data for match {match_id} was not found. "
                "Run python scripts/build_dashboard_data.py "
                f"--match-id {match_id}."
            ),
        ) from exc
