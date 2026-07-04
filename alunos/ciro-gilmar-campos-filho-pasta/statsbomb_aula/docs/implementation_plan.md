# Plano de Implementação: Tradução dos Países (StatsBomb Dashboard)

Este plano descreve as modificações necessárias para traduzir os nomes dos países (seleções) participantes da Copa do Mundo de 2022 para o português, tanto nas listagens e menus da interface quanto nos gráficos renderizados pelo Matplotlib.

## Mudanças Propostas

### 1. Camada de Serviço & Parser

#### [MODIFY] [statsbomb_parser.py](file:///c:/Users/Ciro%20Campos/OneDrive/Documentos/Aula%20CBF/Aula_Cbf-master/Aula_Cbf-master/alunos/ciro-gilmar-campos-filho-pasta/statsbomb_aula/app/services/statsbomb_parser.py)
- Adicionar um dicionário de mapeamento `TEAM_TRANSLATIONS` contendo as traduções dos 32 países da Copa do Mundo de 2022.
- Adicionar a função auxiliar `translate_team(name)` para retornar o nome traduzido ou o original caso não conste no dicionário.

### 2. Rotas da API

#### [MODIFY] [routes.py](file:///c:/Users/Ciro%20Campos/OneDrive/Documentos/Aula%20CBF/Aula_Cbf-master/Aula_Cbf-master/alunos/ciro-gilmar-campos-filho-pasta/statsbomb_aula/app/api/routes.py)
- **Endpoint `/api/matches`**: Traduzir os campos `home_team` e `away_team` antes de enviar o JSON para o frontend.
- **Endpoint `/api/matches/{match_id}`**: 
  - Manter as variáveis em inglês (`home_team_en`, `away_team_en`) para filtros internos e cálculo de métricas avançadas (para não quebrar a lógica com os eventos brutos).
  - Obter as traduções em português (`home_team_pt`, `away_team_pt`) para passar à visualização do fluxo de xG (`plot_xg_flow`).
- **Endpoint `/api/matches/{match_id}/players`**: Traduzir as chaves do dicionário de retorno (nome das seleções nos grupos de dropdown do frontend).
- **Endpoint `/api/matches/{match_id}/players/{player_id}`**: Traduzir o campo `team` do dicionário de estatísticas do jogador (`player_stats["team"]`).

### 3. Visualização de Gráficos (Plotter)

#### [MODIFY] [plotter.py](file:///c:/Users/Ciro%20Campos/OneDrive/Documentos/Aula%20CBF/Aula_Cbf-master/Aula_Cbf-master/alunos/ciro-gilmar-campos-filho-pasta/statsbomb_aula/app/services/plotter.py)
- **Função `plot_jointgrid_shotmap`**: Traduzir os nomes das seleções usados como rótulo (`label`) na legenda do gráfico de finalizações.
- **Função `plot_pass_network`**: Traduzir o nome do time no título do gráfico da rede de passes.

---

## Plano de Verificação

### Testes Automatizados
- Executar `uv run pytest app/tests/ -v` na pasta `statsbomb_aula` para garantir que as rotas da API continuam íntegras e sem erros de execução.

### Verificação Manual
- Acessar o dashboard local (http://127.0.0.1:8080) e verificar se:
  1. A lista de partidas na barra lateral mostra os nomes em português (ex: "França vs Dinamarca", "Argentina vs Arábia Saudita").
  2. O placar principal exibe os nomes traduzidos.
  3. Os gráficos de **Fluxo de xG**, **Rede de Passes** e **Mapa de Finalizações** renderizam os nomes em português nas legendas e títulos.
  4. O dropdown de seleção de jogadores no painel do jogador exibe os grupos de seleções traduzidos.
