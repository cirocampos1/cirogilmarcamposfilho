# Especificação: Desafio 2 - SofaScore interativo

## Objetivo

Evoluir a tela tática para uma comparação de equipes mais próxima do SofaScore, com seleções traduzidas, bandeiras, filtro temporal no menu lateral e mapas interativos por equipe.

## Requisitos

- Exibir nomes das seleções em português na API e no frontend.
- Exibir bandeiras das seleções no placar, lista de partidas e filtros de mapas.
- Exibir datas no formato `dd/mm/yyyy`.
- Exibir jogos no menu lateral com placar embutido, por exemplo `Inglaterra 6-2 Irã`.
- Permitir filtrar partidas por data.
- Exibir comparação de equipes em formato de linhas estatísticas, semelhante à referência SofaScore.
- Permitir filtrar mapas de chutes e passes por `Todos`, mandante ou visitante.
- Cada chute e passe deve ter helper com jogador, minuto e resultado.

## Decisao tecnica

Os JSON brutos StatsBomb serão preservados. A tradução será aplicada em camada de API para evitar inconsistências entre `matches.json`, `events.json`, lineups e nomes usados nos cálculos.

## Validacao

- Teste unitário do contrato de exibição.
- Teste unitário do contrato de eventos interativos.
- Validação Playwright desktop/mobile quando servidor local estiver disponível.
