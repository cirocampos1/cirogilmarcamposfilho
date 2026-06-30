# Especificação: Desafio 2 - Mapas StatsBomb e filtro por jogador

## Objetivo

Corrigir a leitura espacial do mapa de passes, padronizar o campo na convencao
StatsBomb e permitir filtrar por jogador tanto passes quanto chutes.

## Requisitos

- Desenhar o campo no sistema StatsBomb horizontal de `120 x 80`, sem margens
  internas que desloquem os eventos.
- Manter as coordenadas originais dos eventos: `x` no comprimento do campo e
  `y` na largura, com origem no canto superior esquerdo.
- Colorir passe completo em verde e passe incompleto em vermelho,
  independentemente da selecao de equipe.
- Manter espessura e opacidade apenas como apoio de leitura, sem trocar a cor
  pelo time ou pelo criterio de progressao.
- Expor no contrato do evento se o passe foi completo.
- Exibir um unico filtro de jogador reutilizado nos modos Chutes e Passes.
- No mapa de passes, exigir um jogador especifico e nao exibir a opcao de
  todos os jogadores.
- No mapa de chutes, manter a opcao de todos os jogadores.
- Desenhar cada passe como seta, indicando visualmente origem e destino.
- Ocultar o filtro nos modos em que ele nao se aplica, como Penaltis.
- Preservar filtros de equipe e periodo.
- Exibir nos pontos dos radares uma caixa de leitura com nome da metrica, valor
  bruto e valor normalizado.
- Permitir abrir a leitura do radar por mouse, teclado e toque.

## Validacao

- Teste do contrato de conclusao e coordenadas dos passes.
- Teste estrutural do template para campo StatsBomb, cores e filtro nos dois
  modos.
- Teste estrutural para setas e tooltip acessivel nos radares.
- Playwright desktop e mobile na tela da partida.
- Nao fazer commit sem autorizacao humana.
