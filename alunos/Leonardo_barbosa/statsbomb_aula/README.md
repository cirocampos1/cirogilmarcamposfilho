# 🏆 StatsBomb FIFA World Cup 2022 Analytics Dashboard

Dashboard interativo de análise tática da **Copa do Mundo FIFA 2022** com estatísticas reais extraídas dos eventos **StatsBomb Open Data**.

## Funcionalidades

- **64 partidas** com chaveamento completo (Fase de Grupos → Final)
- **Estatísticas reais por time**: posse, finalizações, passes, escanteios, faltas, cartões, impedimentos, desarmes, interceptações
- **Métricas avançadas**: xG, passes sob pressão, high turnovers
- **Visualizações**: mapa de finalizações, rede de passes, fluxo de xG, mapa de pressão
- **Design FIFA**: scoreboard, navbar, sidebar com cores oficiais dos times
- **Logos oficiais FotMob** para todas as 32 seleções

## Documentação Completa

→ [docs/PROJECT_DOCUMENTATION.md](docs/PROJECT_DOCUMENTATION.md)

## Execução

```bash
uv sync
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

Acessar: `http://127.0.0.1:8001`
