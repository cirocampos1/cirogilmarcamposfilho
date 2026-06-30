# Especificação: Desafio 2 - Placar, gols e bandeiras reais

## Objetivo

Melhorar o topo do dashboard e a comparacao de jogadores com informacoes mais ricas de jogo e bandeiras reais em SVG local.

## Requisitos

- Exibir o tecnico abaixo do nome de cada selecao no placar principal.
- Exibir gols com jogador e minuto abaixo de cada selecao.
- Trocar as bandeiras geradas por SVGs reais baixados e versionados localmente em `/static/flags`.
- Na comparacao de jogadores, substituir o nome do pais por bandeira ao lado do nome.
- Adicionar radar visual dentro de cada card de comparacao de jogadores.

## Validacao

- Testes unitarios para contrato de gols, tecnicos, flags reais e radares de comparacao.
- Playwright desktop/mobile para placar enriquecido e comparacao com radar.
- Nao fazer commit sem autorizacao humana.
