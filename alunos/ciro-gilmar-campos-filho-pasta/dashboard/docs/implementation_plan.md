# Plano de Implementação: Exercício 1 — Suporte a Múltiplas Partidas

Este plano descreve as modificações para permitir a exibição e seleção de múltiplas partidas no SofaScore Dashboard, resolvendo a limitação de mostrar apenas uma única partida fixa.

## Proposed Changes

### Banco de Dados & Ingestão

#### [MODIFY] [persist.py](file:///c:/Users/Ciro%20Campos/OneDrive/Documentos/Aula%20CBF/Aula_Cbf-master/Aula_Cbf-master/alunos/ciro-gilmar-campos-filho-pasta/dashboard/app/infra/persist.py)
- Ajustar a rotina de persistência para varrer dinamicamente a pasta `data/raw/match_*` e cadastrar todas as partidas encontradas.
- Ingerir também a partida padrão `16130149` (França vs Irlanda do Norte) localizada em `data/sofascore/` a partir de seu `match_info.json` e `lineups.json`.

### Backend API

#### [MODIFY] [routes.py](file:///c:/Users/Ciro%20Campos/OneDrive/Documentos/Aula%20CBF/Aula_Cbf-master/Aula_Cbf-master/alunos/ciro-gilmar-campos-filho-pasta/dashboard/app/api/routes.py)
- Alterar as funções auxiliares (como `data_dir_match`) para aceitar o `match_id` como parâmetro e retornar a pasta correspondente (ou usar a pasta fallback `sofascore`).
- Garantir que a API de dados do dashboard `/api/dashboard-data` e o endpoint `/api/players` processem corretamente o `match_id` enviado.

## Verification Plan

### Automated Tests
- Executaremos `uv run pytest` para verificar se os testes de API passam com as modificações aplicadas.

### Manual Verification
- Iniciaremos o servidor FastAPI local.
- Utilizaremos o navegador para verificar que o dropdown de partidas carrega os três jogos (`França vs Irlanda`, `Brasil vs Egito` e `França vs Irlanda do Norte`) e que ao alternar de partida, a lista de jogadores correspondente é carregada dinamicamente.
