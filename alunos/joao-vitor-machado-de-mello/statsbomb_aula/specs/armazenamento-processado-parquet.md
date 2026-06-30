# Armazenamento processado do dashboard com Parquet

## Objetivo

Reduzir o tamanho dos dados processados e o custo de carregamento sem alterar
o contrato da API consumido pela interface atual.

## Contrato de armazenamento

- Manter em JSON somente documentos pequenos:
  - `manifest.json`
  - `match_summary.json`
  - `tactical_insights.json`
  - `xg_flow.json`
  - `pressure_maps.json`
- Armazenar em Parquet os dados tabulares ou repetitivos:
  - `tournament_reference.parquet`
  - `events.parquet`
  - `team_metrics.parquet`
  - `player_metrics.parquet`
  - `shot_map.parquet`
  - `pass_map.parquet`
  - `carries.parquet`
  - `pressures.parquet`
  - `momentum.parquet`
  - `player_action_maps.parquet`
- Usar compressão Zstandard e recorrer ao Snappy somente quando Zstandard não
  for aceito pelo mecanismo Parquet instalado.
- Não manter cópia JSON de uma tabela após a gravação bem-sucedida do Parquet.
- `player_metrics.parquet` é a fonte canônica dos dados completos dos
  jogadores. A comparação e os nove radares de destaque reutilizam esse
  arquivo em vez de persistirem duplicações.

## Contrato de compatibilidade

- Os carregadores públicos continuam retornando os mesmos formatos `dict` e
  `list[dict]` esperados pela API e pelo navegador.
- Valores aninhados são serializados em colunas Parquet e restaurados somente
  em memória.
- Durante a execução, as rotas leem apenas `data/processed/`; os JSONs brutos
  da StatsBomb são entradas exclusivas da etapa de construção.
- Os carregadores mantêm cache por caminho e identificador da partida.

## Contrato de tipos e desempenho

- Usar inteiros compactos para identificadores e campos de tempo quando seguro.
- Usar `float32` para colunas decimais.
- Habilitar codificação por dicionário para textos repetidos.
- Reconstruções removem artefatos JSON ou tabulares obsoletos.
- A construção completa deve produzir uma pasta `data/processed/` menor que a
  referência anterior de 222 MB baseada em JSON.

## Validação

- Testes unitários verificam compressão, restauração de valores aninhados e
  formatos retornados pelos carregadores.
- A reconstrução das 64 partidas não contém duplicações JSON dos artefatos
  Parquet.
- A API e o dashboard em desktop e mobile são validados após a reconstrução.
