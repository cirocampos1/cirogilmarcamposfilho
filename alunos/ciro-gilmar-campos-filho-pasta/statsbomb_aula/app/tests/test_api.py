from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_matches():
    response = client.get("/api/matches")
    assert response.status_code == 200
    data = response.json()
    assert "matches" in data
    assert len(data["matches"]) > 0

def test_get_match_detail():
    # Use the test match ID 3857296
    response = client.get("/api/matches/3857296")
    assert response.status_code == 200
    data = response.json()
    assert data["match_id"] == 3857296
    assert "summary" in data
    assert "images" in data
    assert "shotmap" in data["images"]
    assert "pass_network" in data["images"]

def test_get_match_players():
    response = client.get("/api/matches/3857296/players")
    assert response.status_code == 200
    data = response.json()
    assert len(data.keys()) > 0
    # There should be two teams in the match
    for team, players in data.items():
        assert len(players) > 0
        assert "player_id" in players[0]
        assert "name" in players[0]

def test_get_player_detail():
    # Use player 2954 in match 3857296
    response = client.get("/api/matches/3857296/players/2954")
    assert response.status_code == 200
    data = response.json()
    assert data["player_id"] == "2954"
    assert "stats" in data
    assert "radar" in data
    assert "images" in data
    assert "heatmap" in data["images"]
    assert "passmap" in data["images"]
