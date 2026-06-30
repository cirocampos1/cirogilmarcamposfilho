from app.api import routes


def test_normalize_match_id_uses_default():
    assert routes.normalize_match_id() == routes.MATCH_ID


def test_dedupe_players_keeps_last_name_and_sorts():
    players = routes.dedupe_players([
        {"id": "2", "name": "Bia"},
        {"id": "1", "name": "Ana"},
        {"id": "2", "name": "Bruna"},
    ])

    assert players == [
        {"id": "1", "name": "Ana"},
        {"id": "2", "name": "Bruna"},
    ]


def test_cache_returns_copy():
    key = ("unit", "copy")
    value = {"items": [{"name": "original"}]}
    routes.set_cache(key, value)

    cached = routes.get_cache(key)
    cached["items"][0]["name"] = "mutated"

    assert routes.get_cache(key)["items"][0]["name"] == "original"


def test_merge_stats_fills_empty_database_values_from_json():
    merged = routes.merge_stats(
        {"rating": 6.5, "totalPass": 0, "duelWon": None},
        {"rating": 6.1, "totalPass": 7, "duelWon": 1},
    )

    assert merged == {"rating": 6.5, "totalPass": 7, "duelWon": 1}


def test_resolve_match_team_name_prefers_inferred_name_over_generic_db_name():
    lineup_side = {
        "players": [
            {"player": {"country": {"name": "Brazil"}}},
            {"player": {"country": {"name": "Brazil"}}},
            {"player": {"country": {"name": "Egypt"}}},
        ]
    }

    assert routes.resolve_match_team_name("Home", lineup_side, "Home") == "Brazil"
