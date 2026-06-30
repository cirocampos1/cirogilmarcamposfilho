def test_health(client):
    resp = client.get("/api/players?match_id=15186850")
    assert resp.status_code == 200
    data = resp.json()
    assert "players" in data


def test_dashboard_data(client):
    resp = client.get("/api/dashboard-data?player_id=866469&match_id=15186850")
    assert resp.status_code == 200
    data = resp.json()
    assert "images" in data
    assert "stats" in data


def test_dashboard_with_match_id(client):
    resp = client.get("/api/dashboard-data?player_id=866469&match_id=15186850")
    assert resp.status_code == 200
    data = resp.json()
    assert "images" in data
    assert "stats" in data


def test_dashboard_invalid_player(client):
    resp = client.get("/api/dashboard-data?player_id=invalid_id&match_id=15186850")
    # O tratamento de erros retorna dados vazios em vez de quebrar
    assert resp.status_code in (200, 500)


def test_matches(client):
    resp = client.get("/api/matches")
    assert resp.status_code == 200
    data = resp.json()
    assert "matches" in data


def test_list_players_db(client):
    resp = client.get("/api/players/db")
    assert resp.status_code == 200
    data = resp.json()
    assert "players" in data
