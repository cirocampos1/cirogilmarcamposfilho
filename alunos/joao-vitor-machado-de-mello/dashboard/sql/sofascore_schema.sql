-- ============================================================
-- SOFASCORE DATA WAREHOUSE — SCHEMA SQL (SQLite)
-- Versão: 1.0
-- Descrição: Persistência de dados de partidas, jogadores,
--   estatísticas individuais e eventos espaciais (passes,
--   chutes, dribles, ações defensivas, conduções).
-- ============================================================

-- Partidas
CREATE TABLE IF NOT EXISTS matches (
    match_id        INTEGER PRIMARY KEY,
    home_team       TEXT    NOT NULL,
    away_team       TEXT    NOT NULL,
    home_score      INTEGER,
    away_score      INTEGER,
    match_date      TEXT,
    competition     TEXT,
    fetched_at      TEXT    DEFAULT (datetime('now'))
);

-- Jogadores (catálogo global)
CREATE TABLE IF NOT EXISTS players (
    player_id       INTEGER PRIMARY KEY,
    name            TEXT    NOT NULL,
    position        TEXT,
    team            TEXT,
    image_url       TEXT
);

-- Relação partida × jogador (escalação + rating + minutos)
CREATE TABLE IF NOT EXISTS match_players (
    match_id        INTEGER NOT NULL,
    player_id       INTEGER NOT NULL,
    team_side       TEXT    NOT NULL,  -- 'home' | 'away'
    is_starter      INTEGER DEFAULT 0,
    shirt_number    INTEGER,
    rating          REAL,
    minutes_played  INTEGER,
    PRIMARY KEY (match_id, player_id),
    FOREIGN KEY (match_id)  REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

-- Estatísticas agregadas por partida × jogador (67+ colunas)
CREATE TABLE IF NOT EXISTS player_statistics (
    id                          INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id                    INTEGER NOT NULL,
    player_id                   INTEGER NOT NULL,
    total_pass                  INTEGER DEFAULT 0,
    accurate_pass               INTEGER DEFAULT 0,
    total_long_balls            INTEGER DEFAULT 0,
    goal_assist                 INTEGER DEFAULT 0,
    accurate_own_half_passes    INTEGER DEFAULT 0,
    total_own_half_passes       INTEGER DEFAULT 0,
    accurate_opposition_half_passes INTEGER DEFAULT 0,
    total_opposition_half_passes    INTEGER DEFAULT 0,
    total_cross                 INTEGER DEFAULT 0,
    accurate_cross              INTEGER DEFAULT 0,
    duel_lost                   INTEGER DEFAULT 0,
    duel_won                    INTEGER DEFAULT 0,
    total_contest               INTEGER DEFAULT 0,
    won_contest                 INTEGER DEFAULT 0,
    big_chance_created          INTEGER DEFAULT 0,
    on_target_scoring_attempt   INTEGER DEFAULT 0,
    goals                       INTEGER DEFAULT 0,
    ball_recovery               INTEGER DEFAULT 0,
    total_tackle                INTEGER DEFAULT 0,
    won_tackle                  INTEGER DEFAULT 0,
    was_fouled                  INTEGER DEFAULT 0,
    fouls                       INTEGER DEFAULT 0,
    shot_off_target             INTEGER DEFAULT 0,
    blocked_scoring_attempt     INTEGER DEFAULT 0,
    total_clearance             INTEGER DEFAULT 0,
    outfielder_block            INTEGER DEFAULT 0,
    error_lead_to_goal          INTEGER DEFAULT 0,
    minutes_played              INTEGER DEFAULT 0,
    rating                      REAL    DEFAULT 0,
    fetched_at                  TEXT    DEFAULT (datetime('now')),
    UNIQUE(match_id, player_id),
    FOREIGN KEY (match_id)  REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

-- Eventos espaciais: passes, dribles, defensivos, conduções
CREATE TABLE IF NOT EXISTS player_events (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id    INTEGER NOT NULL,
    player_id   INTEGER NOT NULL,
    event_type  TEXT    NOT NULL,  -- 'pass' | 'dribble' | 'defensive' | 'ball_carry'
    x           REAL    NOT NULL,
    y           REAL    NOT NULL,
    end_x       REAL,
    end_y       REAL,
    outcome     INTEGER,           -- 1 = sucesso, 0 = falha
    keypass     INTEGER DEFAULT 0,
    is_home     INTEGER DEFAULT 1,
    FOREIGN KEY (match_id)  REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);
CREATE INDEX IF NOT EXISTS idx_events_match_player
    ON player_events(match_id, player_id);

-- Pontos do mapa de calor
CREATE TABLE IF NOT EXISTS heatmap_points (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id    INTEGER NOT NULL,
    player_id   INTEGER NOT NULL,
    x           REAL    NOT NULL,
    y           REAL    NOT NULL,
    FOREIGN KEY (match_id)  REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);
CREATE INDEX IF NOT EXISTS idx_heatmap_match_player
    ON heatmap_points(match_id, player_id);

-- Pontos do mapa de chutes
CREATE TABLE IF NOT EXISTS shotmap_points (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id    INTEGER NOT NULL,
    player_id   INTEGER NOT NULL,
    x           REAL    NOT NULL,
    y           REAL    NOT NULL,
    shot_type   TEXT,   -- 'goal' | 'miss' | 'save' | 'block'
    body_part   TEXT,
    situation   TEXT,
    FOREIGN KEY (match_id)  REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);
CREATE INDEX IF NOT EXISTS idx_shotmap_match_player
    ON shotmap_points(match_id, player_id);
