# 🏆 StatsBomb FIFA World Cup 2022 Analytics Dashboard

## Visão Geral

Dashboard interativo de análise tática da **Copa do Mundo FIFA 2022** usando dados abertos do **StatsBomb**. Desenvolvido com FastAPI + Jinja2, seguindo o design oficial do site da FIFA.

---

## 🚀 Stack Tecnológica

| Camada       | Tecnologia                                             |
|--------------|--------------------------------------------------------|
| Backend      | **Python 3.13 + FastAPI** (uvicorn)                    |
| Templates    | **Jinja2** (server-side HTML rendering)                |
| Frontend     | **HTML5 + CSS3 + Vanilla JS** (sem frameworks)         |
| Gráficos     | **Matplotlib** (shotmaps, pass networks, xG flow)      |
| Dados        | **StatsBomb Open Data** (JSON events)                  |
| Logos        | **FotMob API** (team logo images)                      |
| Server       | **uvicorn** com hot-reload                             |

---

## 📁 Estrutura do Projeto

```
statsbomb_aula/
├── app/
│   ├── api/
│   │   └── routes.py              # Endpoints REST (matches, detail)
│   ├── core/                      # (reservado para configurações)
│   ├── services/
│   │   ├── statsbomb_parser.py    # Extração e cálculo de métricas
│   │   └── plotter.py             # Renderização Matplotlib
│   ├── static/                    # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/
│   │   └── index.html             # Dashboard principal (FIFA-style)
│   └── main.py                    # Entry point FastAPI
├── data/raw/                      # Dados StatsBomb (matches.json + events)
├── docs/                          # Documentação técnica
├── scripts/
│   └── fetch_world_cup_data.py    # Script de download dos dados
├── pyproject.toml                 # Dependências (uv)
└── uv.lock                        # Lockfile
```

---

## 🔌 API Endpoints

### `GET /api/matches`
Retorna as **64 partidas** da Copa do Mundo 2022 agrupadas por fase.

### `GET /api/matches/{match_id}`
Retorna dados completos de uma partida:

```json
{
  "match_id": 3857271,
  "summary": {
    "total_shots": 21,
    "total_passes": 1093,
    "competition_stage": "Group Stage",
    "stadium": "Khalifa International Stadium, Qatar",
    "referee": "Slavko Vinčić",
    "score": "6 - 2",
    "advanced_metrics": {
      "home": { "xg": 2.45, "goals": 6, "passes_under_pressure_total": 45, ... },
      "away": { "xg": 0.98, "goals": 2, ... }
    },
    "detailed_stats": {
      "home": {
        "shots": 13, "shots_on_target": 11, "passes": 854,
        "passes_completed": 748, "possession": 76.7,
        "corners": 0, "fouls": 24, "yellow_cards": 0,
        "red_cards": 0, "offsides": 0, "clearances": 21,
        "interceptions": 19, "tackles": 33, "blocks": 18
      },
      "away": { ... }
    }
  },
  "images": {
    "shotmap": "base64...",
    "pass_network": "base64...",
    "xg_flow": "base64...",
    "pressure_heatmap": "base64..."
  }
}
```

---

## 📊 Funcionalidades Implementadas

### 1. Design FIFA Copas do Mundo
- **Topbar escura** com logo FIFA, navegação estilo `fifa.com`
- **Navbar** com links: Partidas, Classificação, Equipes, Notícias
- **Scoreboard** centralizado com escudos circulares, placar, estágio e status
- **Sidebar** com chaveamento completo: Fase de Grupos (A-H) + Mata-mata (Oitavas à Final)
- **Tabs** de navegação: Estatísticas, Finalizações, Passes, Pressão

### 2. Estatísticas Reais por Time
Métricas calculadas **em tempo real** dos eventos StatsBomb:

| Métrica              | Fonte no Evento StatsBomb                |
|----------------------|------------------------------------------|
| Posse de bola (%)    | Proporção de eventos por time            |
| Finalizações         | `type == "Shot"`                         |
| Finalizações no gol  | `shot_outcome` vazio, Goal, Saved, Post  |
| Passes               | `type == "Pass"`                         |
| Passes completos     | `pass_outcome` vazio                     |
| Escanteios           | `pass_corner == true`                    |
| Faltas cometidas     | `type == "Foul Committed"`               |
| Cartões amarelos     | `Bad Behaviour` + `card == "Yellow"`     |
| Cartões vermelhos    | `Bad Behaviour` + `card == "Red"`        |
| Impedimentos         | `type == "Offside"`                      |
| Desarmes             | `type == "Duel"`                         |
| Interceptações       | `type == "Interception"`                 |
| Cortes (Clearances)  | `type == "Clearance"`                    |
| Bloqueios            | `type == "Block"`                        |
| xG (Expected Goals)  | `shot_statsbomb_xg`                      |

### 3. Métricas Avançadas
- **xG (Expected Goals)** por time, acumulado no fluxo do jogo
- **Passes sob pressão** (completados/totais)
- **High turnovers** (viradas no terço final do campo)

### 4. Visualizações (Matplotlib)
- 🎯 **Mapa de Finalizações** (shotmap com jogadores)
- 🔗 **Rede de Passes** (pass network por jogador)
- 📈 **Fluxo de xG** (cumulativo minuto a minuto)
- 🔥 **Mapa de Pressão** (heatmap de ações de pressão)

### 5. Cores dos Times nas Barras de Estatística
Cada uma das **32 seleções** possui cores primária e secundária mapeadas:

- Brasil: `#009739` / `#FEDD00`
- Argentina: `#75AADB` / `#FCBF49`
- França: `#002395` / `#ED2939`
- ... (32 times mapeados)

As barras de estatística (`stat-bar-home` / `stat-bar-away`) exibem a **cor do time** correspondente, com glow hover e animação slide-in.

### 6. Logos Oficiais (FotMob)
Os escudos são carregados dinamicamente via `images.fotmob.com/image_resources/logo/teamlogo/{ID}_large.png` para todas as 32 seleções.

---

## 🎨 Efeitos CSS Implementados

- **Slide-in animation**: Barras de estatística aparecem sequencialmente com `opacity` + `translateY`
- **Gradient bars**: Barras com cor sólida do time + glow no hover
- **Hover glow**: `box-shadow` com a cor do time ao passar o mouse
- **Scale pulse**: Valores numéricos escalam 1.1x no hover
- **Staggered delays**: Cada linha de stat anima com delay progressivo (50ms a 600ms)
- **Transition cubic-bezier**: `cubic-bezier(0.25, 0.8, 0.25, 1)` para suavidade

---

## 🛠️ Como Executar

```bash
uv sync
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

Acessar: `http://127.0.0.1:8001`

---

## 🔄 Fluxo de Dados

```
1. fetch_world_cup_data.py → data/raw/ (matches.json + match_{id}/events.json)
2. FastAPI server carrega matches.json no GET /api/matches
3. Usuário clica em partida → GET /api/matches/{id}
4. statsbomb_parser.py extrai eventos e calcula métricas
5. plotter.py renderiza gráficos Matplotlib (base64)
6. index.html renderiza dashboard com dados + imagens
```

---

## 🤖 Agentes Envolvidos (CBF Academy)

| Papel             | Agente           | Função                                  |
|-------------------|------------------|-----------------------------------------|
| Orquestrador      | Maestro Leo      | Gerencia o fluxo do desenvolvimento     |
| Desenvolvedor     | opencode (AI)    | Implementação código e documentação     |
| Dados             | StatsBomb        | Fonte oficial de dados de partidas      |

---

## 📋 Próximos Passos Sugeridos

- [ ] Adicionar gráficos **Chart.js** interativos (disparar/fechar ao clicar)
- [ ] Implementar **Player Radars** com comparação jogador a jogador
- [ ] Calcular **xA (Expected Assists)** e passes progressivos
- [ ] Adicionar **PPDA** (Passes por Ação Defensiva) por time
- [ ] Modo **Dark Mode** alternável
- [ ] **Responsividade mobile** aprimorada
- [ ] Testes **Playwright** para validação visual automática
