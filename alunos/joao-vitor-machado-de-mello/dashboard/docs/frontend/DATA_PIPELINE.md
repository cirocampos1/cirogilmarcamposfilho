# Data Pipeline — SofaScore Player Dashboard

## Fluxo de Dados

```
JSON exportado do navegador
    │
    ▼
┌─────────────────────────────────┐
│  DevTools → Network → Save JSON │
│  (coleta manual/controlada)     │
└────────────┬────────────────────┘
             │
    ┌────────▼────────┐
    │  JSON Files     │
    │ data/           │
    │ ├─ sofascore/           │
    │ ├─ sofascore_player_X/  │
    │ └─ raw/match_X/         │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  persist.py     │
    │  (ingest JSON→  │
    │   SQLite)       │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  SQLite DB      │
    │ data/sofascore.db│
    └────────┬────────┘
             │
    ┌────────▼──────────────────┐
    │  backend/main.py          │
    │  (FastAPI)                │
    │  Cache: DB → JSON fallback│
    └────────┬──────────────────┘
             │
    ┌────────▼────────┐
    │  plot_utils.py  │
    │  (mplsoccer →   │
    │   base64 PNG)   │
    └────────┬────────┘
             │
    ┌────────▼──────────────────────┐
    │  api.js → Dashboard.js        │
    │  (ES Modules, Chart.js radar) │
    └───────────────────────────────┘
             │
             ▼
        Browser Render
```

## Fetch Scripts

### JSON por jogador
- **Match ID:** 16130149
- **Trigger:** Manual — exporte as respostas pelo navegador e salve os arquivos
- **Diretório:** `data/sofascore_player_{id}/`
- **Arquivos:**

| Conteúdo | Arquivo |
|----------|---------|
| Heatmap do jogador | `heatmap.json` |
| Chutes do jogador | `shotmap.json` |
| Eventos para passmap/cards | `rating_breakdown.json` |
| Estatísticas do jogador | `statistics.json` |

### `sofascore_extractor.py` (src/)
- **Match ID:** 15691379
- **Uso:** Extração completa de partida (todos os jogadores)
- **Endpoints por jogador:** `statistics`, `shotmap`, `rating`

## Cache Strategy

```
Backend recebe request → /api/dashboard-data?player_id=X
    │
    ├─❶ SQLite: SELECT * FROM player_statistics WHERE ... 
    │   └─ Se existe: retorna dados do banco (rápido)
    │
    ├─❷ JSON files: data/sofascore_player_X/ 
    │   └─ Se existe: retorna dados do JSON local (médio)
    │
    └─❸ Sem cache
        └─ Retorna resposta vazia compatível, sem acessar a rede
```

## ETL (Extract → Transform → Load)

```bash
# 1. Exportar JSONs pelo navegador e salvar em data/sofascore_player_{id}/

# 2. Ingerir JSON → SQLite
uv run python -m app.infra.persist

# 3. Servir (já usa DB automaticamente)
uv run uvicorn app.main:app --port 8000
```
