# Especificação: Desafio 2 - Dashboard Tático Premium

## Objetivo

Evoluir o dashboard FastAPI da Copa do Mundo 2022 para uma experiencia tática premium, responsiva e orientada por dados StatsBomb.

## Escopo desta rodada

- Enriquecer `/api/matches/{match_id}` com métricas avançadas derivadas dos eventos já baixados.
- Expor xA, passes progressivos, carries progressivos, counterpress, PPDA aproximado e radar de jogadores.
- Refatorar a tela principal com dark mode premium, glassmorphism, microinterações, estados de erro/carregamento e layout responsivo.
- Preservar mapas existentes: finalizações, fluxo de xG, rede de passes e mapa de pressão.

## Contrato de dados

O backend deve continuar retornando `summary` e `images`, acrescentando:

- `summary.advanced_metrics.home|away.xa`
- `summary.advanced_metrics.home|away.progressive_passes`
- `summary.advanced_metrics.home|away.progressive_carries`
- `summary.advanced_metrics.home|away.counterpressures`
- `summary.advanced_metrics.home|away.ppda`
- `summary.player_radars[]`
- `summary.tactical_notes[]`

## Validacao

- Importar o app FastAPI sem erro.
- Chamar `/api/matches/{match_id}` com um jogo real.
- Validar tela desktop e mobile com Playwright quando o servidor local estiver acessivel.

## Fora de escopo

- Baixar novamente dados StatsBomb pela rede.
- Alterar estrutura global do repositorio.
- Fazer commit sem autorizacao humana.
