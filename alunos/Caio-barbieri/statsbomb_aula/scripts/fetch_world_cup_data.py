import os
import json
from statsbombpy import sb

# Definir caminhos relativos de forma robusta
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
os.makedirs(DATA_DIR, exist_ok=True)

COMP_ID = 43  # FIFA World Cup
SEASON_ID = 106  # 2022

def main():
    print(f"Fetching matches for competition {COMP_ID}, season {SEASON_ID}...")
    # match_fmt="dict" doesn't work out of the box in statsbombpy. 
    # Usually it returns a DataFrame, so we convert it.
    df_matches = sb.matches(competition_id=COMP_ID, season_id=SEASON_ID)
    
    # Save the master match list
    matches_dict = df_matches.to_dict(orient="records")
    matches_path = os.path.join(DATA_DIR, "matches.json")
    with open(matches_path, "w", encoding="utf-8") as f:
        # Some dates might be pandas timestamps, handle gracefully by default=str
        json.dump(matches_dict, f, ensure_ascii=False, default=str, indent=2)
    print(f"Saved {len(matches_dict)} matches to {matches_path}")

    # Fetch events and lineups for each match
    for idx, match in enumerate(matches_dict):
        match_id = match["match_id"]
        home = match["home_team"]
        away = match["away_team"]
        
        print(f"[{idx+1}/{len(matches_dict)}] Fetching Match {match_id}: {home} vs {away}...")
        
        match_dir = os.path.join(DATA_DIR, f"match_{match_id}")
        os.makedirs(match_dir, exist_ok=True)
        
        events_path = os.path.join(match_dir, "events.json")
        lineups_path = os.path.join(match_dir, "lineups.json")
        
        # Lineups
        if not os.path.exists(lineups_path):
            try:
                lineups = sb.lineups(match_id=match_id)
                # sb.lineups returns a dictionary of DataFrames: {"Home Team": df, "Away Team": df}
                lineups_dict = {}
                for team, df_lineup in lineups.items():
                    lineups_dict[team] = df_lineup.to_dict(orient="records")
                
                with open(lineups_path, "w", encoding="utf-8") as f:
                    json.dump(lineups_dict, f, ensure_ascii=False, default=str, indent=2)
            except Exception as e:
                print(f"Error fetching lineups for match {match_id}: {e}")
                
        # Events
        if not os.path.exists(events_path):
            try:
                df_events = sb.events(match_id=match_id)
                events_dict = df_events.to_dict(orient="records")
                
                with open(events_path, "w", encoding="utf-8") as f:
                    json.dump(events_dict, f, ensure_ascii=False, default=str, indent=2)
            except Exception as e:
                print(f"Error fetching events for match {match_id}: {e}")

    print("Download complete!")

if __name__ == "__main__":
    main()
