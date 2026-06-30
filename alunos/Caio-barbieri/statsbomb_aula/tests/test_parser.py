import pytest
from app.services.statsbomb_parser import is_progressive_pass, calculate_advanced_metrics, calculate_player_statistics

def test_is_progressive_pass():
    # Gol adversário em (120, 40)
    # Caso 1: Passe antes do meio campo (x < 60), precisa avançar >= 30m
    # Inicia em (40, 40) [dist = 80], termina em (71, 40) [dist = 49]. Diff = 31 >= 30 (Verdadeiro)
    assert is_progressive_pass(40, 40, 71, 40) is True
    
    # Inicia em (40, 40) [dist = 80], termina em (69, 40) [dist = 51]. Diff = 29 < 30 (Falso)
    assert is_progressive_pass(40, 40, 69, 40) is False

    # Caso 2: Passe entre meio campo e intermediária (60 <= x < 80), precisa avançar >= 15m
    # Inicia em (70, 40) [dist = 50], termina em (86, 40) [dist = 34]. Diff = 16 >= 15 (Verdadeiro)
    assert is_progressive_pass(70, 40, 86, 40) is True
    
    # Inicia em (70, 40) [dist = 50], termina em (84, 40) [dist = 36]. Diff = 14 < 15 (Falso)
    assert is_progressive_pass(70, 40, 84, 40) is False

    # Caso 3: Passe no terço ofensivo (x >= 80), precisa avançar >= 10m
    # Inicia em (90, 40) [dist = 30], termina in (101, 40) [dist = 19]. Diff = 11 >= 10 (Verdadeiro)
    assert is_progressive_pass(90, 40, 101, 40) is True
    
    # Inicia em (90, 40) [dist = 30], termina em (98, 40) [dist = 22]. Diff = 8 < 10 (Falso)
    assert is_progressive_pass(90, 40, 98, 40) is False


def test_calculate_advanced_metrics():
    # Mock events
    events = [
        # Chute do time da casa (Gol)
        {
            "possession_team": {"name": "Brasil"},
            "type": "Shot",
            "shot_statsbomb_xg": 0.45,
            "shot_outcome": "Goal"
        },
        # Chute do time de fora (Sem gol)
        {
            "possession_team": {"name": "França"},
            "type": "Shot",
            "shot_statsbomb_xg": 0.15,
            "shot_outcome": "Saved"
        },
        # Passe sob pressão (Completo - sem outcome)
        {
            "possession_team": {"name": "Brasil"},
            "type": "Pass",
            "under_pressure": True,
            "pass_outcome": None
        },
        # Passe sob pressão (Incompleto)
        {
            "possession_team": {"name": "Brasil"},
            "type": "Pass",
            "under_pressure": True,
            "pass_outcome": "Incomplete"
        },
        # Recuperação no terço ofensivo (High Turnover)
        {
            "possession_team": {"name": "França"},
            "type": "Interception",
            "location": [85.0, 40.0]
        },
        # --- Eventos para cálculo do PPDA ---
        # Passes da França (away) na sua própria metade de construção (x <= 80)
        {
            "possession_team": {"name": "França"},
            "team": {"name": "França"},
            "type": "Pass",
            "location": [30.0, 20.0]
        },
        {
            "possession_team": {"name": "França"},
            "team": {"name": "França"},
            "type": "Pass",
            "location": [75.0, 30.0]
        },
        # Ação defensiva do Brasil (home) no campo de ataque (x >= 40 da sua perspectiva)
        {
            "possession_team": {"name": "Brasil"},
            "team": {"name": "Brasil"},
            "type": "Duel",
            "location": [82.0, 50.0]
        }
    ]
    
    metrics = calculate_advanced_metrics(events, "Brasil", "França")
    
    assert metrics["home"]["xg"] == 0.45
    assert metrics["home"]["goals"] == 1
    assert metrics["home"]["passes_under_pressure_total"] == 2
    assert metrics["home"]["passes_under_pressure_completed"] == 1
    
    assert metrics["away"]["xg"] == 0.15
    assert metrics["away"]["goals"] == 0
    assert metrics["away"]["high_turnovers"] == 1
    
    # Validação do PPDA:
    # Passes permitidos pela França: 2 passes iniciados em x <= 80.
    # Ações defensivas do Brasil no campo de ataque: 1 duelo em x = 82 >= 40.
    # PPDA = 2 / 1 = 2.0
    assert metrics["home"]["ppda"] == 2.0


def test_calculate_player_statistics():
    events = [
        # Chute do Jogador 1 (Brasil)
        {
            "player": {"id": 10, "name": "Neymar"},
            "team": {"name": "Brasil"},
            "type": "Shot",
            "shot_statsbomb_xg": 0.35,
            "shot_outcome": "Goal"
        },
        # Passe sob pressão do Jogador 2 (Brasil)
        {
            "player": {"id": 8, "name": "Paquetá"},
            "team": {"name": "Brasil"},
            "type": "Pass",
            "under_pressure": True,
            "pass_outcome": None
        }
    ]
    
    stats = calculate_player_statistics(events)
    
    assert 10 in stats
    assert stats[10]["name"] == "Neymar"
    assert stats[10]["xg"] == 0.35
    assert stats[10]["goals"] == 1
    assert stats[10]["team"] == "Brasil"
    
    assert 8 in stats
    assert stats[8]["name"] == "Paquetá"
    assert stats[8]["passes_under_pressure_total"] == 1
    assert stats[8]["passes_under_pressure_completed"] == 1
    assert stats[8]["team"] == "Brasil"
