# Visual patterns

Selecionar visual a partir da pergunta de negócio e da natureza do dado.

## Série temporal

Usar para responder:
- como o indicador evolui ao longo do tempo?
- quando começou a mudança?

Padrões recomendados:
- linha para tendência
- coluna para comparação de períodos discretos
- linha com meta para desvio versus objetivo

## Comparação entre categorias

Usar para responder:
- quem performa melhor ou pior?
- qual categoria pesa mais?

Padrões recomendados:
- barras horizontais para ranking
- colunas para poucas categorias
- barras empilhadas apenas quando a composição realmente importar

## Composição

Usar para responder:
- de onde vem o total?
- como o mix muda?

Padrões recomendados:
- barras empilhadas
- waterfall quando a variação entre total inicial e final importar
- evitar pizza com muitas categorias

## Funil

Usar para responder:
- onde a conversão se perde entre etapas?

Padrões recomendados:
- funil quando a leitura de queda entre etapas for o foco
- tabela com volume e conversão por etapa quando precisão for mais importante que impacto visual

## Desvio versus meta

Usar para responder:
- estamos acima ou abaixo do esperado?
- qual área mais desvia?

Padrões recomendados:
- bullet chart, quando disponível
- coluna com linha de meta
- tabela com variação absoluta e percentual para detalhe

## Distribuição

Usar para responder:
- como os casos se espalham?
- onde estão outliers?

Padrões recomendados:
- histograma
- boxplot, quando o público aceitar esse tipo de leitura

## Tabela

Usar quando a decisão exigir precisão, detalhe operacional, auditoria ou exportação.
Não usar tabela como substituta de toda a lógica analítica do dashboard.

## Alertas

Sugerir alertas quando houver:
- meta explícita
- limiar operacional claro
- risco relevante de atraso, perda, inadimplência, ruptura ou queda de conversão

Preferir alertas acionáveis, com condição e impacto legíveis.

## Layout

Aplicar a estrutura abaixo como padrão:

1. topo: contexto, filtros globais, kpis-resumo e alertas
2. meio: análise das principais alavancas ou causas
3. base: detalhe, ranking, tabelas e drill-downs

Separar páginas quando o painel misturar consumo executivo e operação diária de forma confusa.
