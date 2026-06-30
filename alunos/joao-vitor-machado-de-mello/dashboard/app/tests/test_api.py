def test_health(client):
    resp = client.get("/api/players")
    assert resp.status_code == 200
    data = resp.json()
    assert "players" in data
    assert "source" in data


def test_dashboard_static_assets_are_not_cached(client):
    resp = client.get("/dashboard/assets/js/app.js")
    assert resp.status_code == 200
    assert resp.headers["cache-control"] == "no-store, max-age=0"


def test_dashboard_data(client):
    resp = client.get("/api/dashboard-data?player_id=866469")
    assert resp.status_code == 200
    data = resp.json()
    assert "images" in data
    assert "stats" in data
    assert "events" in data
    assert "source" in data


def test_dashboard_data_accepts_match_id(client):
    resp = client.get("/api/dashboard-data?player_id=866469&match_id=15691379")
    assert resp.status_code == 200
    data = resp.json()
    assert data["match_id"] == "15691379"


def test_matches(client):
    resp = client.get("/api/matches")
    assert resp.status_code == 200
    data = resp.json()
    assert "matches" in data
    assert len(data["matches"]) >= 1
    match = next(m for m in data["matches"] if m["match_id"] == 15691379)
    assert match["home_team"] == "Brazil"
    assert match["away_team"] == "Egypt"


def test_players_accepts_match_id(client):
    resp = client.get("/api/players?match_id=15691379")
    assert resp.status_code == 200
    data = resp.json()
    assert data["match_id"] == "15691379"


def test_list_players_db(client):
    resp = client.get("/api/players/db")
    assert resp.status_code == 200
    data = resp.json()
    assert "players" in data


def test_compare_players(client):
    resp = client.get("/api/compare?player_ids=866469,1016907&match_id=15691379")
    assert resp.status_code == 200
    data = resp.json()
    assert data["match_id"] == "15691379"
    assert len(data["players"]) == 2
    assert "stats" in data["players"][0]


def test_compare_uses_local_json_when_database_stats_are_partial(client):
    resp = client.get("/api/compare?player_ids=1174937,1016907&match_id=15691379")
    assert resp.status_code == 200
    data = resp.json()
    players = {player["id"]: player for player in data["players"]}

    assert players["1174937"]["stats"]["totalPass"] == 12
    assert players["1016907"]["stats"]["totalPass"] == 7
    assert players["1016907"]["stats"]["ballCarriesCount"] == 4
    assert players["1016907"]["source"] == "database+json"


def test_compare_returns_side_by_side_maps_and_combined_events(client):
    resp = client.get("/api/compare?player_ids=1174937,1016907&match_id=15691379")
    assert resp.status_code == 200
    data = resp.json()

    assert len(data["visuals"]) == 2
    for player in data["visuals"]:
        assert player["images"]["heatmap"]
        assert player["images"]["shotmap"]
        assert player["images"]["passmap"]
    assert len(data["events"]["pass"]) == 19
    assert len(data["events"]["ball_carry"]) == 5
