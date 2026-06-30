# Documentação do Projeto: StatsBomb Analytics

Este documento descreve a arquitetura, os componentes e o fluxo de dados do projeto de análise de dados da Copa do Mundo de 2022, construído utilizando a API de dados abertos do Statsbomb.

## 1. Visão Geral
O projeto é um painel analítico (dashboard) que extrai, processa e visualiza eventos de partidas de futebol usando dados detalhados frame-a-frame e de eventos do Statsbomb. O backend é desenvolvido em Python com FastAPI, e o frontend é em HTML/JS/CSS, consumindo a API localmente.

## 2. Estrutura de Diretórios
Abaixo está a estrutura principal de arquivos dentro de `statsbomb_aula`:

```text
statsbomb_aula/
├── app/
│   ├── api/
│   │   └── routes.py           # Definição dos endpoints da API FastAPI
│   ├── services/
│   │   ├── statsbomb_parser.py # Lógica de extração e cálculo de KPIs
│   │   └── plotter.py          # Lógica de renderização de gráficos usando mplsoccer
│   ├── templates/
│   │   └── index.html          # Interface do usuário (Dashboard)
│   └── main.py                 # Arquivo de inicialização do servidor FastAPI
├── docs/
│   └── PROJECT_DOCUMENTATION.md# Esta documentação
```

## 3. Componentes Principais

### 3.1. Processamento de Dados (`statsbomb_parser.py`)
Este módulo é responsável por buscar os dados do Statsbomb e aplicar as regras de negócio para as métricas.
- **Funções principais:**
  - `get_wc_matches()`: Busca e formata todas as partidas da Copa do Mundo FIFA 2022 (competition_id=43, season_id=106).
  - `calculate_advanced_metrics(events_df)`: Calcula métricas agregadas por time:
    - **Expected Goals (xG)**: Acúmulo de probabilidade de gol baseado nas posições das finalizações.
    - **High Turnovers**: Bolas recuperadas no terço ofensivo.
    - **Passes sob Pressão**: Quantidade e porcentagem de acerto em passes com a flag `under_pressure`.
  - `extract_xg_flow(events_df)`: Filtra as finalizações em ordem cronológica e cria a série temporal do xG.

### 3.2. Motor de Visualização (`plotter.py`)
Utiliza as bibliotecas `mplsoccer`, `matplotlib` e `seaborn` para gerar os mapas de campo. A saída de cada função é a imagem codificada em base64.
- **Gráficos Suportados:**
  - `plot_shot_map(events_df, match_id)`: Um mapa de calor de finalizações simples.
  - `plot_xg_flow(xg_flow_data)`: Gráfico de degraus (*step plot*) que ilustra a dinâmica ofensiva no tempo.
  - `plot_pass_network(events_df, home_team, away_team)`: Rede complexa de passes onde o tamanho dos nós representa volume de participações (recepções/passes) e as arestas representam as conexões mais fortes.
  - `plot_pressure_heatmap(events_df)`: Usa um KDE (Kernel Density Estimation) para desenhar mapas de calor nas regiões do campo onde ocorreu mais "Pressure".

### 3.3. API (`routes.py` e `main.py`)
A API expõe o serviço para o frontend.
- **Endpoints:**
  - `GET /api/matches`: Retorna a lista de 64 partidas da Copa do Mundo 2022 com os dados de cabeçalho.
  - `GET /api/matches/{match_id}`: Retorna um JSON robusto contendo `advanced_metrics` e `plots_base64` gerados dinamicamente para a partida específica.

### 3.4. Frontend (`index.html`)
Painel interativo estruturado com CSS Grid e Vanilla JS.
- Possui uma barra lateral com as partidas.
- Apresenta um cabeçalho de jogo melhorado (Data, Estádio, Placar).
- Exibe KPIs em cartões rápidos de leitura (xG, High Turnovers, Passes sob Pressão).
- Contém contêineres de imagem interativos com as renderizações em base64 do Matplotlib.

## 4. Dependências
As principais bibliotecas exigidas são gerenciadas via `uv`:
- `fastapi` e `uvicorn` (Backend web)
- `statsbombpy` (Extração de dados abertos)
- `pandas` (Manipulação de Dataframes)
- `mplsoccer` e `matplotlib` (Plotagem de campos e gráficos)
- `seaborn` (KDE Plots para calor)
- `jinja2` (Template engine)

---
*Documentação gerada automaticamente para o projeto Statsbomb Analytics.*
