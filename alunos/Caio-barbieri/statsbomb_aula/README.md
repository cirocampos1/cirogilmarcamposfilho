<div align="center">
  <img src="../../images/CBF_Academy_COLORIDA_FUNDO_ESCURO@4x.webp" alt="CBF Academy" width="120"/>

  # 🏆 World Cup 2022 Tactical Analytics

  **Dashboard analítico de performance e tática com dados do StatsBomb — CBF Academy**

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
    <img src="https://img.shields.io/badge/mplsoccer-1.6+-FF6F00?style=for-the-badge&logo=python&logoColor=white" alt="mplsoccer"/>
    <img src="https://img.shields.io/badge/Chart.js-4.0+-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="Chart.js"/>
    <img src="https://img.shields.io/badge/tests-3%2F3%20passed%20✅-10b981?style=flat-square" alt="Tests"/>
    <img src="https://img.shields.io/badge/Desafio-2-1A78CF?style=flat-square" alt="Desafio"/>
  </p>

  <br/>
</div>

---

## 📋 Visão Geral

Este projeto é a evolução tática do painel analítico da Copa do Mundo FIFA 2022 (Desafio 2). Ele extrai, processa e visualiza eventos frame-a-frame de dados abertos do **StatsBomb**, calculando KPIs coletivos avançados, plotando mapas táticos no backend (via `mplsoccer`) e permitindo a comparação interativa de performance de jogadores via radar.

Desenvolvido por **Caio Barbieri** como trabalho final prático para a disciplina **Python para Dados** da **CBF Academy**.

---

## ✨ Features Premium (Nível 110%)

<table>
  <tr>
    <td width="33%" align="center">
      <strong>📊 Radar de Performance</strong><br/>
      Comparação visual lado a lado usando Chart.js (com normalização de 0 a 100% pelo máximo da partida).
    </td>
    <td width="33%" align="center">
      <strong>🧠 Destaques de Duelo</strong><br/>
      Destaque visual automático e em tempo real em verde esmeralda no jogador com a melhor estatística em cada atributo.
    </td>
    <td width="33%" align="center">
      <strong>🏃 Passes Progressivos</strong><br/>
      Algoritmo espacial que mede a progressão efetiva da posse em direção ao gol oponente nas 3 faixas do campo.
    </td>
  </tr>
  <tr>
    <td width="33%" align="center">
      <strong>⏱️ PPDA & Counterpress</strong><br/>
      Cálculo do PPDA (Passes Per Defensive Action) para medir a intensidade de pressão alta de ambas as equipes.
    </td>
    <td width="33%" align="center">
      <strong>🎨 Design WOW Premium</strong><br/>
      Layout responsivo com Glassmorphic CSS, Dark Mode, tipografia Outfit e micro-animações suaves de hover.
    </td>
    <td width="33%" align="center">
      <strong>🗺️ Mapas de Jogo</strong><br/>
      Shotmap (JointGrid/KDE), xG Flow (degraus), Pass Network (grafos) e Pressure Heatmap.
    </td>
  </tr>
</table>

---

## 🏗️ Arquitetura do Sistema

```
┌──────────────────────────────────────────────────────────────────┐
│                    FRONTEND SPA (Vanilla JS + HTML5)             │
│  Modular ES Modules · Chart.js · CSS Glassmorphism · Outfit Font │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  app.js              → Entrypoint, orquestração e APIs        │ │
│  │  PlayerSelector.js   → Carregamento e filtros por equipe      │ │
│  │  StatsRadar.js        → Radar + Tabela e destaques dinâmicos   │ │
│  └──────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬───────────────────────────────────────┘
                           │ HTTP JSON API
┌──────────────────────────▼───────────────────────────────────────┐
│                    FASTAPI BACKEND                                │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  main.py             → Configuração, CORS, Jinja2 e Static     │ │
│  │  api/routes.py       → Endpoints analíticos /api/matches       │ │
│  │  services/plotter.py → Renderização de imagens (base64 plots)  │ │
│  │  services/parser.py  → Lógica matemática e métricas avançadas  │ │
│  └──────────────────────────────────────────────────────────────┘ │
└──────────────────────────┬───────────────────────────────────────┘
                           │ Arquivos JSON Locais
┌──────────────────────────▼───────────────────────────────────────┐
│                    DATA LAYER (StatsBomb Raw JSONs)               │
│  data/raw/matches.json    → Metadados e catálogo de 64 partidas   │
│  data/raw/match_{id}/     → events.json & lineups.json por jogo   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Como Iniciar e Executar

### 1. Pré-requisitos
Certifique-se de ter o Python 3.12+ instalado. Recomendamos o uso do **uv** para gerenciar o ambiente de forma rápida.

### 2. Instalação de Dependências
Do diretório deste projeto (`alunos/Caio-barbieri/statsbomb_aula`), execute:
```bash
uv sync
```

### 3. Execução do Servidor local
Inicie o servidor FastAPI em modo de desenvolvimento (com recarregamento automático):
```bash
.venv\Scripts\python.exe -m uvicorn app.main:app --port 8000 --reload
```
Acesse **`http://localhost:8000/`** no seu navegador.

---

## 📡 Referência da API local

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/` | Retorna o frontend do dashboard |
| `GET` | `/api/matches` | Lista todas as partidas salvas localmente |
| `GET` | `/api/matches/{match_id}` | Retorna o resumo, estatísticas de jogadores e os 4 mapas em base64 |

---

## 🧪 Suíte de Testes Unitários

Para rodar os testes automatizados da lógica do parser (incluindo PPDA e Passes Progressivos), vá até a raiz do monorepo e execute:
```bash
$env:PYTHONPATH="alunos/Caio-barbieri/statsbomb_aula"; .venv\Scripts\pytest.exe alunos/Caio-barbieri/statsbomb_aula/tests/
```

Resultados esperados:
```text
collected 3 items

alunos/Caio-barbieri/statsbomb_aula/tests/test_parser.py ...         [100%]

========================= 3 passed in 0.03s =========================
```

---

## 👨‍🏫 Sobre
Este projeto foi desenvolvido como material prático do curso **Python para Dados** da **CBF Academy**, demonstrando:
- Manipulação e parser de dados brutos esportivos em formato JSON.
- Modelagem de métricas de futebol profissional (xG, xA, PPDA e progressividade de passes).
- Geração dinâmica de plots táticos complexos em backend.
- Construção de SPA reativa com design premium, limpo e profissional.

---

<div align="center">
  <sub>
    Feito com ⚽ e 💻 por Caio Barbieri — 
    <a href="https://www.cbf.com.br/cbf-academy">CBF Academy</a>
  </sub>
  <br/>
  <img src="../../images/CBF_Academy_COLORIDA_FUNDO_ESCURO@4x.webp" width="60"/>
</div>
