<div align="center">
  <img src="../images/CBF_Academy_COLORIDA_FUNDO_ESCURO@4x.webp" alt="CBF Academy" width="120"/>

  # ⚽ SofaScore Player Dashboard

  **Dashboard de análise de performance de futebol — CBF Academy**

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/FastAPI-0.135-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
    <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
    <img src="https://img.shields.io/badge/mplsoccer-1.6-FF6F00?style=for-the-badge&logo=python&logoColor=white" alt="mplsoccer"/>
    <img src="https://img.shields.io/badge/Playwright-1.58-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" alt="Playwright"/>
    <img src="https://img.shields.io/badge/license-MIT-10b981?style=for-the-badge" alt="License"/>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/tests-18%2F18%20✅-10b981?style=flat-square" alt="Tests"/>
    <img src="https://img.shields.io/badge/status-production-10b981?style=flat-square" alt="Status"/>
  </p>

  <br/>
</div>

---

## 📋 Visão Geral

Dashboard interativo que lê dados **reais exportados do SofaScore em JSON local**, armazena em cache **SQLite** e exibe visualizações táticas profissionais — mapas de calor, chutes, passes, eventos e estatísticas detalhadas — em uma SPA moderna com design **glassmorphism**.

> Projeto didático desenvolvido durante o curso **Python para Dados** da **CBF Academy**.

---

## ✨ Features

<table>
  <tr>
    <td width="33%" align="center">
      <strong>🗺️ Mapas Táticos</strong><br/>
      Heatmap (kdeplot), Shotmap (scatter por tipo), Passmap (setas) — em coordenadas Opta
    </td>
    <td width="33%" align="center">
      <strong>📊 Radar de Performance</strong><br/>
      Chart.js com radar/barras, filtros, comparação entre jogadores e merge DB+JSON
    </td>
    <td width="33%" align="center">
      <strong>🧠 Cache Inteligente</strong><br/>
      SQLite → JSON local → resposta vazia compatível
    </td>
  </tr>
  <tr>
    <td width="33%" align="center">
      <strong>🎨 Design Glassmorphism</strong><br/>
      Tema escuro, vidro fosco, gradientes, animações suaves
    </td>
    <td width="33%" align="center">
      <strong>🔌 API REST</strong><br/>
      Endpoints de partidas, jogadores, dashboard e comparação
    </td>
    <td width="33%" align="center">
      <strong>📁 Ingestão Offline</strong><br/>
      Ingestão manual/controlada a partir de JSON exportado do navegador
    </td>
  </tr>
</table>

---

## ✅ Entrega do Desafio

Itens da seção **"O que melhorar?"** implementados nesta versão:

| Item | Implementação |
|------|---------------|
| O dashboard só mostra 1 partida fixa | `/api/matches`, `match_id` nos endpoints e seletor de partida no frontend. |
| O frontend é bonito mas estático | Gráfico Chart.js alternando entre radar e barras. |
| Eventos mostram passes e dribles — e filtros? | Filtros de eventos por todos, passes, dribles, defesa e conduções. |
| Não tem comparação entre jogadores | Seletor de comparação, endpoint `/api/compare`, gráfico comparativo, resumo por jogador e mapas lado a lado. |
| API sem cache | Cache em memória com TTL + SQLite + fallback para JSON local. |
| Zero tratamento de erro no frontend | Timeout com `AbortController`, mensagens de erro e estado vazio consistente. |
| Só 7 testes | Suíte ampliada para 18 testes cobrindo API, cache, helpers, comparação, mapas lado a lado, nomes de equipes, assets sem cache e banco. |
| Não tem container | `Dockerfile` para build e execução sem depender de `uv`. |

---

## 🧭 SDD / Orquestra

Esta entrega foi guiada pelo `orquestra.md` usando Spec-Driven Development:

| Fase SDD | Aplicação nesta entrega |
|----------|--------------------------|
| S1 — Especificação | Contrato: melhorar o dashboard dentro de `dashboard/`, sem alterar a estrutura de `alunos/`, cobrindo todos os itens do desafio. |
| S2 — Planejamento | Separação por camadas: API/cache/dados, frontend/interação, testes, Docker e documentação. |
| S2.5 — TDD | Testes adicionados para `match_id`, comparação, mapas lado a lado, merge de estatísticas parciais e cache defensivo. |
| S3 — Tarefas | Implementação dividida em partidas, gráfico, filtros, comparação, cache, erro, cobertura e container. |
| S4 — Implementação | FastAPI + SQLite/JSON local, SPA em JS modular, Chart.js e Docker. |
| S5 — Validação | `pytest` no container, `py_compile` no backend e validação visual com Playwright. |

Decisões de segurança e governança:

- Sem escrita em produção e sem chamadas automatizadas ao SofaScore em runtime.
- Fallback offline para JSON local, evitando bloqueios 403/challenge.
- Sem commit automático; revisão humana continua obrigatória.

---

## 🏗️ Arquitetura

```
┌──────────────────────────────────────────────────────────────────┐
│                    FRONTEND SPA                                   │
│  Vanilla JS (ES Modules) · Chart.js · CSS Glassmorphism           │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  PlayerSelector  │  Dashboard  │  StatsRadar                │ │
│  │  (dropdown)      │  (3 maps)   │  (Chart.js canvas)         │ │
│  └──────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬───────────────────────────────────────┘
                           │ HTTP REST (JSON)
┌──────────────────────────▼───────────────────────────────────────┐
│                    FASTAPI BACKEND                                │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  main.py         → App factory · CORS · Static mount         │ │
│  │  api/routes.py   → endpoints REST (APIRouter)               │ │
│  │  services/       → mplsoccer: heatmap, shotmap, passmap     │ │
│  │  infra/          → DatabaseService + persist (ETL)          │ │
│  │  fetchers/       → leitores/importadores de JSON local      │ │
│  │  cli/            → fetch_player · download_image            │ │
│  └──────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬───────────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────────┐
│                    DATA LAYER                                     │
│  SQLite (data/sofascore.db) — 7 tabelas, 847 registros            │
│  JSON (data/raw/ + data/sofascore_player_*/)                      │
│  Schema DDL em sql/sofascore_schema.sql                           │
└──────────────────────────┬───────────────────────────────────────┘
                           │ JSON exportado do navegador
┌──────────────────────────▼───────────────────────────────────────┐
│                    IMPORT LAYER                                   │
│  DevTools/Network → JSON local → persist.py                       │
│  app/cli/fetch_player.py — valida JSONs locais do jogador         │
│  app/fetchers/sofascore.py — leitor de contrato JSON              │
└──────────────────────────────────────────────────────────────────┘
```

### Fluxo de Requisição

```
Usuário                        Backend                          Cache
   │                              │                               │
   ├── GET /api/dashboard-data ──►│                               │
   │                              ├──► DB: stats? heatmap? ─────►│
   │                              │◄── cache HIT ────────────────│
   │                              ├──► sem cache → JSON files     │
   │                              ├──► sem JSON → vazio compatível│
   │◄── response (images + stats)─┤                               │
```

---

## 🚀 Quick Start

### Pré-requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

### Setup

```bash
# 1. Entrar no projeto
cd dashboard

# 2. Instalar dependências
uv sync

# 3. Ingerir dados (opcional — após salvar JSONs locais)
uv run python -m app.infra.persist

# 4. Iniciar servidor
uv run uvicorn app.main:app --reload --port 8000

# 5. Abrir no navegador
open http://127.0.0.1:8000/dashboard/
```

### Comandos CLI

```bash
# Validar JSONs locais de um jogador
uv run python -m app.cli.fetch_player 866469

# Download de imagem do jogador
uv run python -m app.cli.download_image 866469 15691379

# Ingestão completa dos JSONs para SQLite
uv run python -m app.infra.persist
```

### Docker sem uv

```bash
cd dashboard
docker build -t sofascore-dashboard .
docker run --rm -p 8000:8000 sofascore-dashboard
```

---

## 📡 API

### Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/players?match_id=X` | Lista jogadores da partida (DB → lineups → JSON local) |
| `GET` | `/api/dashboard-data?player_id=X&match_id=Y` | Dashboard completo: imagens + stats + eventos |
| `GET` | `/api/compare?player_ids=A,B&match_id=Y` | Compara jogadores e retorna gráfico, mapas lado a lado e eventos combinados |
| `GET` | `/api/matches` | Partidas cadastradas ou encontradas em JSON local |
| `GET` | `/api/players/db` | Jogadores no banco SQLite |
| `GET` | `/dashboard/` | Frontend SPA (static mount) |
| `GET` | `/docs` | Swagger UI (automático) |
| `GET` | `/redoc` | ReDoc (automático) |

### Exemplo: `/api/dashboard-data?player_id=866469&match_id=15691379`

```json
{
  "match_id": "15691379",
  "player_id": "866469",
  "images": {
    "heatmap": "base64...",
    "shotmap": "base64...",
    "passmap": "base64..."
  },
  "stats": {
    "rating": 7.2,
    "minutesPlayed": 90,
    "totalPass": 45,
    "accuratePass": 38,
    "goals": 1,
    "onTargetScoringAttempt": 3,
    "duelWon": 12,
    "duelLost": 4,
    "wonTackle": 5,
    "interceptions": 8
  },
  "events": {
    "pass": [
      {
        "playerCoordinates": {"x": 50, "y": 30},
        "passEndCoordinates": {"x": 78, "y": 45},
        "outcome": true,
        "keypass": false
      }
    ],
    "dribble": [],
    "defensive": [],
    "ball_carry": []
  },
  "source": "database+json"
}
```

> **Nota:** As imagens (heatmap, shotmap, passmap) são retornadas como **base64** — prontas para uso direto no atributo `src` de uma tag `<img>`.

---

## 🗄️ Database

**Engine:** SQLite (zero-config, sem servidor) — `data/sofascore.db`

### Schema (7 tabelas)

| Tabela | Registros | Finalidade |
|--------|----------|------------|
| `matches` | 1 | Partidas |
| `players` | 51 | Jogadores |
| `match_players` | 44 | Relação partida-jogador |
| `player_statistics` | 42 | Estatísticas detalhadas (29 campos) |
| `player_events` | 359 | Passes, dribles, defensivas, carregamentos |
| `heatmap_points` | 277 | Pontos de calor (coordenadas Opta) |
| `shotmap_points` | 26 | Chutes (coordenadas + tipo) |

DDL completo: `sql/sofascore_schema.sql`

---

## 🧪 Testes

```bash
cd dashboard
uv run pytest app/tests/ -v
```

```
collected 18 items

app/tests/test_api.py .........                           [ 56%]
app/tests/test_database.py ...                            [ 75%]
app/tests/test_routes_helpers.py ....                     [100%]

======================== 18 passed ========================
```

---

## 🧰 Stack

| Categoria | Tecnologia |
|-----------|------------|
| **Runtime** | Python 3.13+ |
| **Framework Web** | FastAPI + Uvicorn |
| **Banco** | SQLite (cache-first) |
| **Frontend** | Vanilla JS (ES Modules) + Chart.js |
| **CSS** | Glassmorphism · Outfit Font · CSS Modules |
| **Plotagem** | mplsoccer (coordenadas Opta) |
| **Ingestão** | JSON local exportado do navegador |
| **Package** | uv · Hatchling · Workspace |

---

## 📁 Estrutura

```
dashboard/
├── app/                           # ★ Código principal
│   ├── main.py                   # FastAPI app factory
│   ├── api/routes.py             # REST endpoints (APIRouter)
│   ├── services/plotter.py       # mplsoccer: heatmap, shotmap, passmap
│   ├── infra/
│   │   ├── database.py           # DatabaseService (SQLite)
│   │   └── persist.py            # ETL: JSON → SQLite
│   ├── fetchers/
│   │   ├── sofascore.py          # Leitor de JSON local
│   │   └── extractor.py          # Extrator de partida (sync)
│   ├── cli/
│   │   ├── fetch_player.py       # CLI: valida JSONs do jogador
│   │   └── download_image.py     # CLI: download de imagem
│   ├── frontend/                 # SPA (static mount)
│   │   ├── index.html
│   │   ├── assets/css/           # 3 módulos CSS
│   │   └── assets/js/            # 5 módulos JS
│   └── tests/                    # 18 testes pytest
├── data/                         # SQLite + JSON
├── sql/                          # Schema DDL
├── docs/                         # Documentação detalhada
├── pyproject.toml                # Dependências
└── README.md                     # ← Você está aqui
```

---

## 🎨 Design System

| Token | Valor | Uso |
|-------|-------|-----|
| `--bg-color` | `#0f172a` | Background principal |
| `--accent` | `#10b981` | Verde esmeralda (destaque) |
| `--panel-bg` | `rgba(30,41,59,0.7)` | Painéis glassmorphism |
| `--text-main` | `#f8fafc` | Texto primário |
| **Fonte** | Outfit (Google Fonts) | Pesos: 300, 400, 600, 800 |

> Design system completo: [`app/frontend/design-system/MASTER.md`](app/frontend/design-system/MASTER.md)

---

## 📚 Documentação

| Documento | Conteúdo |
|-----------|----------|
| [`docs/README.md`](docs/README.md) | Índice da documentação |
| [`docs/frontend/ARCHITECTURE.md`](docs/frontend/ARCHITECTURE.md) | Arquitetura de componentes e data flow |
| [`docs/frontend/DATA_PIPELINE.md`](docs/frontend/DATA_PIPELINE.md) | Pipeline de dados completo |
| [`docs/api/REST.md`](docs/api/REST.md) | Referência completa da API |
| [`docs/database/README.md`](docs/database/README.md) | Overview do banco e estratégia de cache |
| [`docs/database/SCHEMA.md`](docs/database/SCHEMA.md) | Schema detalhado (colunas, tipos, índices) |

---

## 👨‍🏫 Sobre

Este projeto foi desenvolvido como material didático do curso **Python para Dados** da **CBF Academy**, demonstrando na prática:

- Pipeline offline a partir de JSON exportado do navegador
- Pipeline ETL completo (JSON → SQLite → REST)
- Visualização de dados esportivos com mplsoccer
- API REST com FastAPI
- Frontend SPA com JavaScript modular e design glassmorphism
- Testes automatizados com pytest

---

<div align="center">
  <sub>
    Feito com ⚽ durante o curso Python para Dados — 
    <a href="https://www.cbf.com.br/cbf-academy">CBF Academy</a>
  </sub>
  <br/>
  <img src="../images/CBF_Academy_COLORIDA_FUNDO_ESCURO@4x.webp" width="60"/>
</div>
