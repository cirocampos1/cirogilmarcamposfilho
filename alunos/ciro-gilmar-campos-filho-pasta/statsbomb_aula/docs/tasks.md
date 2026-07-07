# Tarefas: Tradução dos Países (StatsBomb Dashboard)

- [x] Adicionar `TEAM_TRANSLATIONS` e `translate_team` em `statsbomb_parser.py`
- [x] Modificar `/api/matches` para traduzir times em `routes.py`
- [x] Modificar `/api/matches/{match_id}` para suportar labels em português em `routes.py`
- [x] Modificar `/api/matches/{match_id}/players` para agrupar com chaves em português em `routes.py`
- [x] Modificar `/api/matches/{match_id}/players/{player_id}` para traduzir time do jogador em `routes.py`
- [x] Atualizar `plot_jointgrid_shotmap` em `plotter.py` para usar labels em português
- [x] Atualizar `plot_pass_network` em `plotter.py` para usar título com nome em português
- [x] Executar testes de API para validar integridade
- [x] Verificar no navegador se os nomes e gráficos aparecem traduzidos
- [x] Formatar as datas no padrão Dia/mês/ano (DD/MM/YYYY)
