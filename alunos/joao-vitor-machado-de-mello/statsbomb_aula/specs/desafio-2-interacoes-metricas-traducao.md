# Especificação: Desafio 2 - Interações, métricas e tradução

## Objetivo

Refinar o dashboard tatico com melhor leitura em portugues, gols agrupados, ordenacao cronologica, chutes-gol destacados e graficos mais interativos.

## Requisitos

- Remover o bloco inferior de gols do placar, mantendo somente data, estadio e arbitro.
- Agrupar gols repetidos do mesmo jogador em uma unica linha com todos os minutos.
- Destacar finalizacoes que viraram gol no mapa de chutes com formato diferente.
- Traduzir fases, labels taticos e metricas como carries/counterpress.
- Adicionar helpers curtos para PPDA, impacto/influencia e counterpress.
- Ordenar lista de jogos por data e horario em ordem ascendente.
- Tornar radars e fluxo xG mais explicativos via tooltip/hover.
- Expor no fluxo xG minuto e valor acumulado por time.
- Adicionar metricas de passes certos, precisao de passes, dribles certos, desarmes certos e chutes no alvo.
- Quando possivel, usar cores derivadas das selecoes nos graficos interativos.

## Validacao

- Testes de contrato para ordenacao, fases traduzidas, gols agrupados e novas metricas.
- Validacao visual desktop/mobile com Playwright.
- Graphify deve ser consultado/atualizado quando disponivel; se ausente, registrar bloqueio.
