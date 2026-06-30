# Especificação: Desafio 2 - Períodos, jogadores e bandeiras

## Objetivo

Remover elementos nao funcionais da interface, tornar os filtros de tempo reais, melhorar o mapa de passes com foco por jogador, criar comparacao de jogadores e substituir os badges de bandeira por imagens SVG locais.

## Requisitos

- Remover a barra visual `Formacoes / Estatisticas / Classificacao / H2H`.
- Manter `Todos / 1º / 2º` apenas como filtro real para estatisticas e eventos.
- O mapa de passes deve ser filtrado por jogador, evitando o desenho geral ilegivel.
- O mapa de passes deve descartar passes sem coordenadas validas dentro do campo.
- Criar secao de comparacao entre dois jogadores do jogo.
- Trocar badges CSS de bandeira por imagens SVG locais servidas em `/static/flags`.

## Validacao

- Testes unitarios do contrato de periodos, eventos e jogadores.
- Playwright desktop/mobile para mapa por jogador, filtros de periodo e comparacao.
- Sem commit automatico.
