# REST API — SofaScore Player Dashboard

**Base URL:** `http://127.0.0.1:8000`

## Endpoints

### `GET /api/players?match_id=15691379`
Retorna lista de jogadores disponíveis para a partida (ordenada por nome).

**Response:**
```json
{
  "players": [
    { "id": "866469", "name": "Bruno Guimarães" },
    { "id": "124992", "name": "Danilo" }
  ]
}
```

**Data source:** Banco SQLite → `match_players JOIN players` → `lineups.json` → diretórios `sofascore_player_*`.

---

### `GET /api/dashboard-data?player_id=866469&match_id=15691379`
Retorna dados completos do dashboard para um jogador.

**Response:**
```json
{
  "match_id": "15691379",
  "player_id": "866469",
  "images": {
    "heatmap": "base64...",     // PNG do mapa de calor
    "shotmap": "base64...",     // PNG do mapa de chutes
    "passmap": "base64..."      // PNG do mapa de passes
  },
  "stats": {
    "rating": 8.1,
    "minutesPlayed": 45,
    "totalPass": 35,
    "accuratePass": 33,
    "goalAssist": 0,
    "totalCross": 2,
    "duelWon": 4,
    "duelLost": 2,
    "totalTackle": 1,
    "wonTackle": 1,
    "interceptions": 6,
    "wasFouled": 2,
    "goals": 1,
    "onTargetScoringAttempt": 1,
    "shotOffTarget": 0,
    "blockedScoringAttempt": 0,
    "clearances": 0,
    "fouls": 1
  },
  "events": {
    "passes": [          // Máx 50 eventos
      {
        "playerCoordinates": { "x": 36.3, "y": 51.1 },
        "passEndCoordinates": { "x": 33.0, "y": 56.9 },
        "outcome": true,
        "keypass": false,
        "isHome": true
      }
    ],
    "dribbles": [],      // Máx 20
    "defensive": [],      // Máx 20
    "ball_carries": []    // Máx 20
  },
  "source": "database"
}
```

**Cache strategy:**
1. SQLite (cache principal)
2. JSON files (fallback)
3. Cache em memória por 60s para respostas frequentes

Não há fetch automático online nesse fluxo. Se SQLite e JSON local não tiverem
dados, a resposta permanece compatível com o frontend, mas retorna mapas vazios
e `"source": "empty"`.

**JSON local esperado:**

Diretório por jogador:

```text
data/sofascore_player_<PLAYER_ID>/
  heatmap.json
  shotmap.json
  statistics.json
  rating_breakdown.json
```

Formato mínimo:

```json
{
  "heatmap.json": {
    "heatmap": [{ "x": 42.1, "y": 55.8 }]
  },
  "shotmap.json": {
    "shotmap": [
      {
        "playerCoordinates": { "x": 88.0, "y": 44.0 },
        "shotType": "goal"
      }
    ]
  },
  "statistics.json": {
    "statistics": {
      "rating": 7.2,
      "minutesPlayed": 90,
      "totalPass": 45,
      "accuratePass": 38,
      "ballRecovery": 8
    }
  },
  "rating_breakdown.json": {
    "passes": [
      {
        "playerCoordinates": { "x": 36.3, "y": 51.1 },
        "passEndCoordinates": { "x": 62.0, "y": 49.0 },
        "outcome": true,
        "keypass": false,
        "isHome": true
      }
    ],
    "dribbles": [],
    "defensive": [],
    "ball-carries": []
  }
}
```

Cada bloco acima deve ser salvo em seu próprio arquivo. O exemplo está agrupado
apenas para mostrar o contrato.

---

### `GET /api/matches`
Retorna partidas no banco de dados e partidas descobertas em `data/raw/match_*`.

**Response:**
```json
{
  "matches": [
    {
      "match_id": 15691379,
      "home_team": "Brasil",
      "away_team": "Egito",
      "match_date": "2024",
      "competition": "Friendly"
    }
  ]
}
```

---

### `GET /api/compare?player_ids=866469,1016907&match_id=15691379`
Retorna estatísticas lado a lado, mapas individuais por jogador e eventos combinados para comparação.

**Response:**
```json
{
  "match_id": "15691379",
  "players": [
    {
      "id": "866469",
      "name": "Bruno Guimarães",
      "stats": {
        "rating": 7.2,
        "totalPass": 45,
        "duelWon": 12
      },
      "source": "database"
    }
  ],
  "visuals": [
    {
      "id": "866469",
      "name": "Bruno Guimarães",
      "images": {
        "heatmap": "base64...",
        "shotmap": "base64...",
        "passmap": "base64..."
      }
    },
    {
      "id": "1016907",
      "name": "Igor Thiago",
      "images": {
        "heatmap": "base64...",
        "shotmap": "base64...",
        "passmap": "base64..."
      }
    }
  ],
  "events": {
    "pass": [],
    "dribble": [],
    "defensive": [],
    "ball_carry": []
  },
  "source": "comparison"
}
```

---

### `GET /api/players/db`
Retorna todos os jogadores do banco de dados (com posição).

**Response:**
```json
{
  "players": [
    {
      "player_id": 866469,
      "name": "Bruno Guimarães",
      "position": "M",
      "team": null,
      "image_url": null
    }
  ]
}
```

---

### `GET /dashboard/`
Serve o frontend SPA (arquivos estáticos do diretório `frontend/`).
