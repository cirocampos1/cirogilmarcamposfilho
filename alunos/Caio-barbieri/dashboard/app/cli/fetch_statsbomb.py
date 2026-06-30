import os
import json
import urllib.request
from datetime import datetime
from app.infra.database import DatabaseService

MATCHES_URL = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/43/106.json"
LINEUP_URL_TEMPLATE = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/lineups/{match_id}.json"
EVENTS_URL_TEMPLATE = "https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/{match_id}.json"

def scale_x(x_sb):
    return min(100.0, max(0.0, (x_sb / 120.0) * 100.0))

def scale_y(y_sb):
    return min(100.0, max(0.0, (y_sb / 80.0) * 100.0))

def main():
    print("Iniciando ingestão de dados do StatsBomb (Copa 2022 - Jogos do Brasil)...")
    db = DatabaseService()
    
    # 1. Obter partidas
    try:
        with urllib.request.urlopen(MATCHES_URL) as r:
            matches_data = json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Erro ao baixar partidas: {e}")
        return

    brazil_matches = []
    for m in matches_data:
        home = m.get("home_team", {}).get("home_team_name")
        away = m.get("away_team", {}).get("away_team_name")
        if home == "Brazil" or away == "Brazil":
            brazil_matches.append(m)

    print(f"Encontradas {len(brazil_matches)} partidas do Brasil.")

    for m in brazil_matches:
        match_id = m["match_id"]
        home_team = m["home_team"]["home_team_name"]
        away_team = m["away_team"]["away_team_name"]
        home_score = m["home_score"]
        away_score = m["away_score"]
        match_date = m["match_date"]
        competition = "World Cup 2022"

        print(f"\nProcessando Partida {match_id}: {home_team} {home_score} x {away_score} {away_team} ({match_date})")

        # Inserir partida no banco
        db.upsert_match(
            match_id=match_id,
            home_team=home_team,
            away_team=away_team,
            home_score=home_score,
            away_score=away_score,
            match_date=match_date,
            competition=competition
        )

        # 2. Obter escalações (lineups)
        lineup_url = LINEUP_URL_TEMPLATE.format(match_id=match_id)
        try:
            with urllib.request.urlopen(lineup_url) as r:
                lineups = json.loads(r.read().decode('utf-8'))
        except Exception as e:
            print(f"Erro ao baixar escalações da partida {match_id}: {e}")
            continue

        player_map = {} # player_id -> name, side, position, shirt
        for team_lineup in lineups:
            team_name = team_lineup["team_name"]
            side = "home" if team_name == home_team else "away"
            for p in team_lineup["lineup"]:
                p_id = p["player_id"]
                p_name = p["player_name"]
                shirt = p["jersey_number"]
                
                # Encontrar a posição principal e se é titular
                is_starter = 0
                position_name = "Substituto"
                for pos in p.get("positions", []):
                    if pos.get("start_reason") == "Starting XI":
                        is_starter = 1
                    position_name = pos.get("position", position_name)

                # Cadastrar jogador no banco global
                db.upsert_player(
                    player_id=p_id,
                    name=p_name,
                    position=position_name,
                    team=team_name
                )
                
                # Guardar para processamento local
                player_map[p_id] = {
                    "name": p_name,
                    "side": side,
                    "position": position_name,
                    "shirt": shirt,
                    "is_starter": is_starter,
                    "minutes": 90 if is_starter else 0
                }

        # 3. Obter eventos
        events_url = EVENTS_URL_TEMPLATE.format(match_id=match_id)
        try:
            with urllib.request.urlopen(events_url) as r:
                events = json.loads(r.read().decode('utf-8'))
        except Exception as e:
            print(f"Erro ao baixar eventos da partida {match_id}: {e}")
            continue

        print(f"Total de {len(events)} eventos baixados.")

        # Dicionários de estatísticas e mapas por jogador
        player_stats = {}      # player_id -> dict de estatísticas
        player_heatmaps = {}   # player_id -> list de pontos (x, y)
        player_shotmaps = {}   # player_id -> list de chutes
        player_event_lists = {} # player_id -> dict de tipos de eventos

        # Inicializa estruturas para jogadores do player_map
        for p_id in player_map:
            player_stats[p_id] = {
                "total_pass": 0, "accurate_pass": 0, "total_long_balls": 0, "goal_assist": 0,
                "accurate_own_half_passes": 0, "total_own_half_passes": 0,
                "accurate_opposition_half_passes": 0, "total_opposition_half_passes": 0,
                "total_cross": 0, "accurate_cross": 0, "duel_lost": 0, "duel_won": 0,
                "total_contest": 0, "won_contest": 0, "big_chance_created": 0,
                "on_target_scoring_attempt": 0, "goals": 0, "ball_recovery": 0,
                "total_tackle": 0, "won_tackle": 0, "was_fouled": 0, "fouls": 0,
                "shot_off_target": 0, "blocked_scoring_attempt": 0, "total_clearance": 0,
                "outfielder_block": 0, "error_lead_to_goal": 0, "minutes_played": 0, "rating": 6.0
            }
            player_heatmaps[p_id] = []
            player_shotmaps[p_id] = []
            player_event_lists[p_id] = {
                "pass": [], "dribble": [], "defensive": [], "ball_carry": []
            }

        # Processar cada evento
        for ev in events:
            player_info = ev.get("player")
            if not player_info:
                continue
            
            p_id = player_info["id"]
            # Caso o jogador não esteja mapeado na escalação (raro, mas por garantia)
            if p_id not in player_stats:
                continue

            loc = ev.get("location")
            x_opta = scale_x(loc[0]) if loc else None
            y_opta = scale_y(loc[1]) if loc else None

            # Adicionar ao heatmap se houver localização
            if x_opta is not None:
                player_heatmaps[p_id].append({"x": x_opta, "y": y_opta})

            ev_type = ev.get("type", {}).get("name")
            is_home = (player_map[p_id]["side"] == "home")

            # 3.1. PASSES
            if ev_type == "Pass":
                pass_data = ev.get("pass", {})
                outcome_info = pass_data.get("outcome")
                # Se outcome_info não existir, o passe foi completo
                outcome = (outcome_info is None)
                keypass = bool(pass_data.get("assisted_shot_id"))
                assist = bool(pass_data.get("goal_assist"))
                cross = bool(pass_data.get("cross"))
                
                player_stats[p_id]["total_pass"] += 1
                if outcome:
                    player_stats[p_id]["accurate_pass"] += 1
                
                if pass_data.get("length", 0) > 25.0:
                    player_stats[p_id]["total_long_balls"] += 1
                if cross:
                    player_stats[p_id]["total_cross"] += 1
                    if outcome:
                        player_stats[p_id]["accurate_cross"] += 1
                if assist:
                    player_stats[p_id]["goal_assist"] += 1
                if keypass:
                    player_stats[p_id]["big_chance_created"] += 1

                # Determinar metade do campo (StatsBomb x vai de 0 a 120, metade é 60)
                # Na perspectiva do time que ataca, 0-60 é campo de defesa, 60-120 é ataque.
                # Como a localização está no formato original do StatsBomb:
                start_x_sb = loc[0] if loc else 0
                if start_x_sb < 60.0:
                    player_stats[p_id]["total_own_half_passes"] += 1
                    if outcome:
                        player_stats[p_id]["accurate_own_half_passes"] += 1
                else:
                    player_stats[p_id]["total_opposition_half_passes"] += 1
                    if outcome:
                        player_stats[p_id]["accurate_opposition_half_passes"] += 1

                # Mapear coordenadas de fim
                end_loc = pass_data.get("end_location")
                end_x = scale_x(end_loc[0]) if end_loc else None
                end_y = scale_y(end_loc[1]) if end_loc else None

                player_event_lists[p_id]["pass"].append({
                    "playerCoordinates": {"x": x_opta, "y": y_opta},
                    "passEndCoordinates": {"x": end_x, "y": end_y},
                    "outcome": outcome,
                    "keypass": keypass,
                    "isHome": is_home
                })

            # 3.2. CHUTES
            elif ev_type == "Shot":
                shot_data = ev.get("shot", {})
                shot_outcome = shot_data.get("outcome", {}).get("name")
                is_goal = (shot_outcome == "Goal")

                shot_type_mapped = "miss"
                if is_goal:
                    shot_type_mapped = "goal"
                    player_stats[p_id]["goals"] += 1
                elif shot_outcome in ("Saved", "Saved to Post", "Saved Off Target"):
                    shot_type_mapped = "save"
                    player_stats[p_id]["on_target_scoring_attempt"] += 1
                elif shot_outcome == "Blocked":
                    shot_type_mapped = "block"
                    player_stats[p_id]["blocked_scoring_attempt"] += 1
                else:
                    player_stats[p_id]["shot_off_target"] += 1

                player_shotmaps[p_id].append({
                    "playerCoordinates": {"x": x_opta, "y": y_opta},
                    "shotType": shot_type_mapped
                })

            # 3.3. DRIBLES
            elif ev_type == "Dribble":
                dribble_data = ev.get("dribble", {})
                outcome = (dribble_data.get("outcome", {}).get("name") == "Complete")
                
                player_stats[p_id]["total_contest"] += 1
                if outcome:
                    player_stats[p_id]["won_contest"] += 1

                player_event_lists[p_id]["dribble"].append({
                    "playerCoordinates": {"x": x_opta, "y": y_opta},
                    "outcome": outcome,
                    "isHome": is_home
                })

            # 3.4. CONDUÇÕES (CARRY)
            elif ev_type == "Carry":
                carry_data = ev.get("carry", {})
                end_loc = carry_data.get("end_location")
                end_x = scale_x(end_loc[0]) if end_loc else None
                end_y = scale_y(end_loc[1]) if end_loc else None

                player_event_lists[p_id]["ball_carry"].append({
                    "playerCoordinates": {"x": x_opta, "y": y_opta},
                    "passEndCoordinates": {"x": end_x, "y": end_y},
                    "outcome": True,
                    "isHome": is_home
                })

            # 3.5. DEFENSIVO: DESARMES, RECUPERAÇÕES, INTERCEPTAÇÕES E CORTES
            elif ev_type in ("Ball Recovery", "Interception", "Clearance", "Block", "Duel"):
                is_defensive_event = False
                
                if ev_type == "Duel":
                    duel_data = ev.get("duel", {})
                    duel_type = duel_data.get("type", {}).get("name")
                    duel_outcome = duel_data.get("outcome", {}).get("name")
                    is_tackle = (duel_type == "Tackle")
                    
                    if is_tackle:
                        is_defensive_event = True
                        player_stats[p_id]["total_tackle"] += 1
                        # Sucesso no desarme
                        if duel_outcome in ("Won", "Success In Play", "Success Out of Play"):
                            player_stats[p_id]["won_tackle"] += 1
                            player_stats[p_id]["duel_won"] += 1
                        else:
                            player_stats[p_id]["duel_lost"] += 1
                    else:
                        # Duelo aéreo ou terrestre comum
                        if duel_outcome in ("Won", "Success In Play", "Success Out of Play", "Success"):
                            player_stats[p_id]["duel_won"] += 1
                        else:
                            player_stats[p_id]["duel_lost"] += 1
                
                elif ev_type == "Ball Recovery":
                    is_defensive_event = True
                    player_stats[p_id]["ball_recovery"] += 1
                
                elif ev_type == "Interception":
                    is_defensive_event = True
                    player_stats[p_id]["ball_recovery"] += 1 # Conta também como recuperação
                
                elif ev_type == "Clearance":
                    is_defensive_event = True
                    player_stats[p_id]["total_clearance"] += 1
                
                elif ev_type == "Block":
                    is_defensive_event = True
                    player_stats[p_id]["outfielder_block"] += 1

                # Adiciona à lista de eventos defensivos
                if is_defensive_event and x_opta is not None:
                    player_event_lists[p_id]["defensive"].append({
                        "playerCoordinates": {"x": x_opta, "y": y_opta},
                        "outcome": True,
                        "isHome": is_home
                    })

            # 3.6. FALTAS
            elif ev_type == "Foul Committed":
                player_stats[p_id]["fouls"] += 1
            elif ev_type == "Foul Won":
                player_stats[p_id]["was_fouled"] += 1

            # 3.7. SUBSTITUIÇÕES E MINUTOS
            elif ev_type == "Substitution":
                sub_data = ev.get("substitution", {})
                replacement_id = sub_data.get("replacement", {}).get("id")
                minute = ev["minute"]
                
                # Substituído sai do jogo
                player_map[p_id]["minutes"] = minute
                
                # Jogador que entra começa agora
                if replacement_id in player_map:
                    player_map[replacement_id]["minutes"] = 90 - minute

        # 4. Gravar os dados calculados de cada jogador no Banco de Dados
        print("Gravando estatísticas dos jogadores no SQLite...")
        for p_id, p_info in player_map.items():
            stats = player_stats[p_id]
            stats["minutes_played"] = p_info["minutes"]
            
            # Cálculo de Rating Personalizado Realista (mínimo 3.0, máximo 10.0)
            acc_pct = stats["accurate_pass"] / stats["total_pass"] if stats["total_pass"] > 0 else 0.7
            custom_rating = (
                6.0 +
                stats["goals"] * 1.5 +
                stats["goal_assist"] * 1.0 +
                stats["big_chance_created"] * 0.4 +
                (acc_pct - 0.7) * 2.0 +
                stats["won_tackle"] * 0.2 +
                stats["ball_recovery"] * 0.1 -
                stats["fouls"] * 0.15 -
                stats["duel_lost"] * 0.05
            )
            stats["rating"] = round(min(10.0, max(3.0, custom_rating)), 1)
            
            # Gravar no banco através do DatabaseService
            db.persist_player_data(
                match_id=match_id,
                player_id=p_id,
                name=p_info["name"],
                team_side=p_info["side"],
                stats_dict=stats,
                events_dict=player_event_lists[p_id],
                heatmap_list=player_heatmaps[p_id],
                shotmap_list=player_shotmaps[p_id],
                rating=stats["rating"],
                minutes=stats["minutes_played"],
                position=p_info["position"]
            )

    print("\nIngestão finalizada com sucesso! Todos os dados da Copa de 2022 para jogos do Brasil foram importados.")

if __name__ == "__main__":
    main()
