# Especificação: Desafio 2 - Ajudas contextuais, modal e pênaltis

## Objetivo

Tornar as métricas individuais explicáveis, permitir ampliar os mapas táticos
e exibir todos os pênaltis de uma partida, incluindo cobranças durante o jogo e
disputas após o tempo regulamentar.

## Requisitos

- Explicar o número de impacto no card de comparação como a soma das métricas
  do perfil posicional do jogador.
- Expandir as abreviações dos chips dos radares por meio de ajuda acessível.
- Adicionar botão para ampliar os mapas de chutes, passes e pênaltis.
- Exibir o mapa ampliado em diálogo acessível, fechável por botão, backdrop e
  tecla Escape.
- Exibir a aba Pênaltis quando houver cobrança durante o jogo ou disputa por
  pênaltis.
- Manter eventos do período 5 separados das métricas normais da partida.
- Revisar os textos visíveis da interface com acentuação e cedilhas.

## Validação

- Teste de contrato para pênaltis regulares e disputas.
- Teste estrutural para ajudas contextuais e diálogo acessível.
- Testes existentes sem regressão.
- Playwright desktop e mobile quando disponível.
- Não fazer commit sem autorização humana.
