# Especificação: Desafio 2 - Mapa de pênaltis e contraste

## Objetivo

Completar a leitura das disputas por penaltis e melhorar comparacao visual de metricas e graficos.

## Requisitos

- Exibir uma terceira aba de mapa, Penaltis, apenas quando houver disputa.
- Plotar o destino de cada cobranca e diferenciar gol, defesa e erro.
- Remover o texto Sem gols quando uma equipe nao marcou.
- Exibir no menu lateral o placar no formato Time (P) G-G (P) Time.
- Manter no dashboard o placar normal e PEN/Penaltis separado abaixo.
- Barras percentuais devem usar escala absoluta de 0 a 100.
- Quando cores principais forem semelhantes, usar cor secundaria do visitante.
- A cor secundaria deve ser realmente distinta da primaria.
- Quando a equipe nao tiver uma segunda cor distinta, usar branco como fallback.
- Substituir o helper simples do fluxo xG por tooltip maior e estilizado.

## Validacao

- Testes para label lateral, dados de destino da cobranca e contraste.
- Playwright desktop/mobile em partida decidida nos penaltis.
- Nao fazer commit sem autorizacao humana.
