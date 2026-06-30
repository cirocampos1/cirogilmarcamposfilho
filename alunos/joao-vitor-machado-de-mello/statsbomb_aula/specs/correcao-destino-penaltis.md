# Especificação: correção do destino das cobranças de pênalti

## Objetivo

Preservar e exibir corretamente as coordenadas de destino das cobranças de
pênalti fornecidas pela StatsBomb.

## Requisitos

- Preservar todas as colunas ao salvar tabelas Parquet com linhas
  heterogêneas.
- Manter `end_y` e `end_z` no contrato dos eventos de pênalti.
- Posicionar cada cobrança na baliza usando `shot_end_location`.
- Não desenhar uma cobrança em uma posição padrão quando o destino estiver
  ausente.
- Manter resultado, equipe, jogador e número da cobrança na interface.
- Corrigir os dados compactados da partida Argentina x França (`3869685`).

## Validação

- Teste de round-trip Parquet com campos existentes apenas nas últimas linhas.
- Teste do contrato de destino das cobranças da final.
- Testes automatizados sem regressão.
- Validação visual desktop da partida `3869685`.
- Não fazer commit sem autorização humana.
