# Especificação: Desafio 2 - Pênaltis e radares por posição

## Objetivo

Separar disputas por penaltis das estatisticas normais da partida e adaptar comparacoes/radares ao papel de cada jogador.

## Requisitos

- Tratar eventos do periodo 5 como disputa por penaltis.
- Exibir placar da disputa separado do placar oficial.
- Excluir disputa por penaltis de gols, xG, mapas e metricas da partida.
- Identificar posicao dominante de cada jogador por eventos, com fallback para lineups.
- Traduzir posicoes e agrupar em goleiro, defensor, meio-campista e atacante.
- Usar seis metricas de radar especificas por grupo posicional.
- Normalizar cada radar apenas contra jogadores do mesmo grupo.
- Exibir posicao nos seletores e cards de comparacao.

## Validacao

- Testes para placar de penaltis e ausencia de contaminacao no xG/gols.
- Testes para posicao e perfil de radar.
- Playwright desktop/mobile em uma partida decidida nos penaltis.
- Nao fazer commit sem autorizacao humana.
