# Especificação — métricas por 90, referência posicional e recorte ofensivo

## Objetivo

Evoluir os mapas e os radares do Desafio 2 para facilitar a leitura espacial dos
eventos ofensivos e permitir comparações de jogadores com métricas ajustadas
pelo tempo em campo.

## Requisitos funcionais

1. Somente o modal ampliado de chutes deve exibir o terço ofensivo do campo
   StatsBomb em proporção panorâmica `2:1`, com o gol no topo. Passes e pênaltis
   preservam suas visualizações ampliadas anteriores.
2. Um passe selecionado deve preservar sua cor de resultado e receber somente
   um contorno branco discreto, sem brilho ou aumento forte de espessura.
3. Os minutos jogados devem ser derivados dos intervalos de posição das
   escalações, usando o fim da partida para intervalos sem horário final.
4. A resposta da partida deve expor, por jogador, minutos, métricas por 90
   minutos e distância longitudinal de progressão.
5. A interface deve apresentar uma tabela separada de métricas por 90 minutos.
6. O radar principal deve usar somente os eventos da partida selecionada,
   normalizados por 90, e sobrepor uma área mais fraca e transparente com a
   média acumulada por 90 dos jogadores do mesmo grupo posicional em todo o
   torneio. A escala de normalização também deve ser única por posição e baseada
   no torneio, permitindo comparação consistente entre jogos. A população de
   referência exige pelo menos 90 minutos acumulados para evitar distorções de
   atletas com participação residual.
7. O gráfico do item C deve incluir a distância total avançada em passes e
   conduções progressivas, nomeada "Distância percorrida em progressão".
8. A barra de PPDA deve ser proporcional ao valor apresentado. Um PPDA maior
   gera uma barra maior, embora o texto preserve a orientação de que valores
   menores representam pressão mais intensa.
9. Os prefixos A, B e C e o título introdutório do dicionário de dados não devem
   aparecer na interface.
10. A tabela por 90 deve permitir ordenação crescente e decrescente por qualquer
    coluna visível.
11. O texto de cada equipe no gráfico defensivo deve apresentar Counterpress
    antes de PPDA, na mesma ordem visual das barras.
12. O mapa de pressão deve separar as equipes e explicar que áreas mais intensas
    representam maior concentração de eventos `Pressure`, com ambas orientadas
    atacando da esquerda para a direita.
13. Cada mapa de pressão deve conter uma seta textual indicando a direção do
    ataque.
14. As barras dos gráficos de criação, intensidade defensiva e progressão devem
    exibir helper no hover/foco com nome da métrica e valor.
15. Os dois cards de comparação devem permanecer dentro de um único bloco e
    oferecer ação para abrir um modal ampliado.
16. O modal de comparação deve usar seis dimensões comuns entre posições:
    Ataque, Criação, Progressão, Passe, Defesa e Pressão. A normalização deve
    usar uma régua geral pré-calculada do torneio.
17. O modal de comparação deve listar métricas lado a lado e destacar o maior
    valor em cada linha.
18. Clicar em um radar de destaque ou em uma linha da tabela deve abrir um modal
    individual com o radar específico da posição, a média posicional do torneio
    em cinza e os valores brutos da partida.
19. A tabela por 90 deve incluir a equipe ao lado do nome do jogador.
20. Os chips exibidos nos cards da seção de radares devem mostrar os totais da
    partida, sem sufixo `/90`; o `/90` permanece apenas no cálculo do radar e da
    referência cinza.
21. Todos os radares devem usar escala contextual de 0 a 100 calculada pela
    distribuição por 90 da macroposição na Copa, sem depender do máximo da partida.
22. A média cinza da macroposição deve usar a mesma escala p05–p95 aplicada ao
    jogador e ser ponderada por minutos.
23. O modal de comparação deve repetir os dois seletores e sincronizar alterações
    com os seletores e cards da tela principal.
24. As barras da visão geral da partida e da comparação simples de jogadores
    devem exibir helper no hover/foco com métrica, equipe ou jogador e valor.
25. A indicação de direção dos mapas de pressão deve aparecer abaixo da imagem
    do campo, não sobre ou acima dela.
26. A normalização por máximo da partida deve permanecer somente em barras e
    rankings. Radares usam distribuição contextual do torneio por macroposição.
27. As macroposições são Goleiro, Zagueiro, Lateral/Ala,
    Volante/Meio-campista, Meia ofensivo/Ponta e Centroavante.
28. Cada métrica contextual usa valores por 90, p05 e p95 da macroposição:
    `score = clamp((valor - p05) / (p95 - p05) * 100, 0, 100)`. Quando
    `p95 <= p05`, o score é 50.
29. Cada métrica do jogador deve expor `raw_value`, `per90_value` e
    `score_0_100`.
30. Radares de linha usam as dimensões Ataque, Criação, Progressão, Passe,
    Defesa e Pressão, calculadas como médias ponderadas de scores individuais.
31. Goleiros usam Defesa do gol, Jogo com os pés, Bolas longas, Ações fora da
    área, Pressão recebida e Participação na construção.
32. Os pesos das métricas e o peso das dimensões no índice de influência podem
    variar por macroposição.
33. A média cinza é ponderada por minutos e transformada pela mesma escala
    p05/p95 usada pelo jogador.
34. Influência é um índice base 100 separado do score: 100 representa a média
    contextual da macroposição.
35. Radar e comparação exigem pelo menos 30 minutos. Rankings exigem pelo menos
    45 minutos. Tabelas mostram todos e sinalizam amostras abaixo de 30 minutos.
36. A comparação ampliada mostra bruto, por 90, score, diferença para média da
    macroposição e um resumo automático de 1 ou 2 frases.
37. Leituras táticas devem incluir números sempre que os dados estiverem
    disponíveis.
38. O mapa de chutes deve permitir Todos, Somente gols e xG alto, preservando
    filtros existentes. O tamanho varia por xG e chutes sem gol têm menor
    opacidade.
39. A comparação ampliada deve organizar métricas em Passe, Progressão,
    Criação, Finalização, Pressão, Defesa e Disciplina.
40. Toda eficiência deve aparecer acompanhada do volume no formato
    `percentual (sucessos/tentativas)`; denominadores nulos retornam `N/D`.
41. A listagem geral deve ser enxuta, filtrável por equipe, posição,
    macroposição, minutos e tipo de métrica, preservando ordenação.
42. O detalhe individual deve incluir radar de perfil, radar de eficiência,
    métricas em três camadas, mapa de ações e eventos principais.
43. O mapa individual deve suportar passes, progressões, conduções, pressões,
    counterpress, recuperações, desarmes, interceptações, chutes e ações
    defensivas.
44. A visão principal deve incluir resumo tático compacto e os maiores impactos,
    sem mover todas as métricas detalhadas para a tela principal.
45. O fluxo temporal deve alternar entre xG, pressão, progressão e finalizações.
46. O mapa de chutes deve também filtrar chutes no alvo e tipo de finalização.
47. Cada métrica relevante deve preservar bruto, por 90, percentual,
    denominador, score contextual e diferença contra a média quando aplicável.
48. O radar de eficiência deve usar percentuais de passe, passe sob pressão,
    drible, desarme, duelo, duelo aéreo, conversão e cruzamento, sempre com
    volume disponível em tooltip ou tabela.
49. Métricas específicas de goleiros e jogadores de linha devem ser derivadas
    somente de campos existentes no StatsBomb Open Data.
50. O processamento analítico deve ocorrer em uma etapa de build, nunca no
    request de seleção de partida.
51. `scripts/build_dashboard_data.py` deve gerar `manifest.json`, referência
    global e artefatos por partida em `data/processed/matches/{match_id}`.
52. A API deve carregar somente o manifest na listagem e somente os artefatos
    da partida selecionada no detalhe.
53. Loaders de artefatos devem usar cache por caminho ou `match_id`.
54. Tabelas grandes devem usar Parquet quando houver engine instalada e JSON
    como fallback reproduzível.
55. O build deve aceitar `--force` e `--match-id`, preservando artefatos válidos
    quando não houver solicitação de rebuild.
56. Os cards de momentum e pressão devem possuir alturas visuais equivalentes,
    com controles de momentum compactos e sem ocupar a altura do gráfico.
57. As paletas cosméticas definidas para Holanda, Japão, Inglaterra, Irã,
    Austrália, Croácia e Alemanha devem ser aplicadas por um catálogo explícito,
    sem alterar as cores usadas para desenhar as bandeiras.
58. A interface deve apresentar totais produzidos na partida e não chamar
    nenhum valor exibido de "por 90 minutos".
59. O filtro de minutos deve começar em 30 e oferecer atalhos de 0, 15, 30, 45,
    60 e 90 minutos.
60. Radares preservam score contextual, mas a legenda deve distinguir jogador
    na partida, média da macroposição na Copa e distribuição da função.
61. Comparação ampliada deve distinguir total do jogo, score contextual e
    influência base 100, com navegação por categoria.
62. Top Impactos deve priorizar três atletas, influência, diferença contra a
    função e justificativa numérica.
63. O mapa de chutes deve explicar círculo, estrela, tamanho por xG e cor por
    equipe; o momentum deve explicitar blocos de cinco minutos.

## Regras de cálculo

- `por_90 = valor / minutos * 90`, retornando zero quando os minutos forem zero.
- A distância progressiva usa apenas o avanço longitudinal positivo:
  `max(0, x_final - x_inicial)`.
- A distância total progressiva é a soma das distâncias de passes e conduções
  classificados como progressivos.
- A média do radar é calculada após a normalização por 90 nas seis
  macroposições e ponderada pelos minutos acumulados.
- Percentuais usam uma função segura: denominador zero produz valor nulo e
  apresentação `N/D`, nunca divisão por zero.
- Passe completo possui `pass_outcome` vazio; chute no alvo usa Goal, Saved ou
  Saved to Post; desarme certo usa os outcomes StatsBomb definidos no contrato.

## Critérios de aceite

- O contrato automatizado cobre minutos, por 90, distância e radar médio.
- O modal de chutes usa `viewBox="0 0 80 40"` e rotação das coordenadas; passes
  preservam o campo completo.
- A seleção de passe possui uma linha de contorno independente.
- A tabela é responsiva, com rolagem horizontal em telas estreitas.
- Testes Python e validação visual desktop/mobile não apresentam regressões.
- Testes da API garantem que nenhuma função analítica pesada é chamada durante
  a leitura de uma partida processada.
