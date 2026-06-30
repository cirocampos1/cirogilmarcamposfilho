# Graph Report - alunos\Caio-barbieri\statsbomb_aula  (2026-06-22)

## Corpus Check
- 18 files · ~17,666 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 94 nodes · 107 edges · 14 communities (11 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2a7238fe`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]

## God Nodes (most connected - your core abstractions)
1. `get_base64_image()` - 6 edges
2. `🤖 Como Orquestrar seu Esquadrão (Guia do Aluno)` - 6 edges
3. `get_pitch()` - 5 edges
4. `PlayerSelector` - 5 edges
5. `StatsRadar` - 5 edges
6. `1. Dicionário de Eventos Principais` - 5 edges
7. `2. O Que Podemos Fazer (Visão Tática / Professor Léo)` - 5 edges
8. `Documentação do Projeto: StatsBomb Analytics` - 5 edges
9. `3. Componentes Principais` - 5 edges
10. `Análise do Tech Lead: Estimativa de Recursos e Custos do Projeto` - 5 edges

## Surprising Connections (you probably didn't know these)
- `test_calculate_advanced_metrics()` --calls--> `calculate_advanced_metrics()`  [EXTRACTED]
  tests/test_parser.py → app/services/statsbomb_parser.py
- `test_is_progressive_pass()` --calls--> `is_progressive_pass()`  [EXTRACTED]
  tests/test_parser.py → app/services/statsbomb_parser.py
- `test_calculate_player_statistics()` --calls--> `calculate_player_statistics()`  [EXTRACTED]
  tests/test_parser.py → app/services/statsbomb_parser.py
- `loadMatch()` --calls--> `fetchMatchDetails()`  [EXTRACTED]
  app/static/js/app.js → app/static/js/services/api.js

## Import Cycles
- None detected.

## Communities (14 total, 3 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.18
Nodes (6): PlayerSelector, StatsRadar, currentMatchPlayersStats, loadMatch(), fetchMatchDetails(), fetchMatches()

### Community 1 - "Community 1"
Cohesion: 0.20
Nodes (10): calculate_advanced_metrics(), calculate_player_statistics(), get_match_events(), get_match_lineups(), get_matches(), is_progressive_pass(), replace_nan(), test_calculate_advanced_metrics() (+2 more)

### Community 2 - "Community 2"
Cohesion: 0.17
Nodes (11): 1.1 Passes (`type.name == "Pass"`), 1.2 Finalizações (`type.name == "Shot"`), 1.3 Conduções (`type.name == "Carry"`), 1.4 Ações Defensivas (`Pressure`, `Duel`, `Interception`, `Clearance`, `Block`), 1. Dicionário de Eventos Principais, 2. O Que Podemos Fazer (Visão Tática / Professor Léo), A. Análise de Construtores de Jogo (Playmakers), B. Análise de Intensidade Defensiva (+3 more)

### Community 3 - "Community 3"
Cohesion: 0.18
Nodes (10): 🤖 Como Orquestrar seu Esquadrão (Guia do Aluno), 🏆 Desafio 2: Evolução Tática do Dashboard (Para Casa), 💡 Dicas de Ouro, 🎯 O Objetivo, Passo 0: Preparando o Vestiário (Setup) 🏟️, Passo 1: Invoque o Maestro Léo 🎼, Passo 2: O Brainstorming 🧠, Passo 3: Ative os Especialistas (UI/UX e Frontend) 🎨 (+2 more)

### Community 4 - "Community 4"
Cohesion: 0.20
Nodes (9): 1. Visão Geral, 2. Estrutura de Diretórios, 3.1. Processamento de Dados (`statsbomb_parser.py`), 3.2. Motor de Visualização (`plotter.py`), 3.3. API (`routes.py` e `main.py`), 3.4. Frontend (`index.html`), 3. Componentes Principais, 4. Dependências (+1 more)

### Community 5 - "Community 5"
Cohesion: 0.25
Nodes (7): 1. Escopo Construído (O Produto), 2. Squad Necessária (Modelo Tradicional), 3.1. Fluxo Tradicional Humano, 3.2. Fluxo Ágil Impulsionado por IA (O que foi executado), 3. Estimativas de Tempo e Custo (Humanos vs. IA), 4. Veredito e Conclusão, Análise do Tech Lead: Estimativa de Recursos e Custos do Projeto

### Community 6 - "Community 6"
Cohesion: 0.61
Nodes (7): get_base64_image(), get_pitch(), plot_jointgrid_shotmap(), plot_pass_network(), plot_pressure_heatmap(), plot_shotmap(), plot_xg_flow()

## Knowledge Gaps
- **30 isolated node(s):** `Request`, `currentMatchPlayersStats`, `Statsbomb World Cup 2022 Dashboard`, `Requisitos do Desafio:`, `Passo 0: Preparando o Vestiário (Setup) 🏟️` (+25 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `Request`, `currentMatchPlayersStats`, `Statsbomb World Cup 2022 Dashboard` to the rest of the system?**
  _30 weakly-connected nodes found - possible documentation gaps or missing edges._