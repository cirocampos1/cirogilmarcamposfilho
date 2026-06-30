# Dashboard tático da Copa do Mundo de 2022

Dashboard web para análise das 64 partidas da Copa do Mundo de 2022 com dados
de eventos da StatsBomb. O projeto reúne:

- API em FastAPI;
- interface responsiva em HTML, CSS e JavaScript;
- mapas de chutes, passes, pênaltis, ações e pressão;
- comparação de equipes e jogadores;
- radares contextualizados pela posição;
- métricas de criação, progressão, pressão e eficiência;
- banco SQLite compacto com todas as partidas já processadas.

O projeto clonado do Git não precisa recalcular métricas nem baixar os JSONs
brutos para funcionar. A execução normal utiliza somente
`data/dashboard.sqlite3`.

## Instalação e execução

### Pré-requisitos

- Python 3.10 ou superior;
- `uv` instalado.

### 1. Instalar as dependências

Na pasta do projeto:

```bash
uv sync
```

O ambiente normal instala apenas as dependências necessárias para executar o
dashboard:

- FastAPI;
- Uvicorn;
- Jinja2.

Bibliotecas analíticas como pandas, PyArrow, Matplotlib e mplsoccer não são
necessárias durante a navegação.

### 2. Iniciar o servidor

```bash
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Acesse:

```text
http://127.0.0.1:8000/
```

Não é necessário executar o script de processamento antes de iniciar o
servidor. O banco versionado já contém as 64 partidas.

## Estrutura de execução

O dashboard distribuído no Git usa um único arquivo:

```text
data/dashboard.sqlite3
```

Esse banco contém:

- o manifesto usado para listar as partidas;
- um payload completo para cada partida;
- os dados de equipes e jogadores;
- mapas e séries temporais;
- radares e comparações;
- leituras táticas;
- imagens dos mapas de pressão.

Cada partida é armazenada individualmente como JSON compactado com `zlib`.
Assim, a API descompacta somente a partida selecionada e mantém o resultado em
cache.

```text
Navegador
    │
    ▼
FastAPI
    │
    ├── lista de partidas
    │       └── manifesto do SQLite
    │
    └── partida selecionada
            └── payload compactado da partida
```

O banco possui aproximadamente 30 MB. Ele substitui, na execução normal, a
árvore anterior com centenas de JSONs e Parquets e os aproximadamente 627 MB
de dados brutos.

## Arquitetura do projeto

```text
statsbomb_aula/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── dashboard_builder.py
│   │   ├── plotter.py
│   │   ├── processed_data.py
│   │   └── statsbomb_parser.py
│   ├── static/
│   ├── templates/
│   │   └── index.html
│   └── main.py
├── data/
│   └── dashboard.sqlite3
├── docs/
├── scripts/
│   ├── build_dashboard_data.py
│   └── fetch_world_cup_data.py
├── specs/
└── tests/
```

### Aplicação web

`app/main.py` cria o FastAPI, registra as rotas, publica os arquivos estáticos
e entrega a página principal.

### Rotas

`app/api/routes.py` disponibiliza:

- `GET /`: interface do dashboard;
- `GET /api/matches`: lista das 64 partidas;
- `GET /api/matches/{match_id}`: dados completos da partida selecionada.

### Carregamento dos dados

`app/services/processed_data.py`:

- consulta primeiro `data/dashboard.sqlite3`;
- descompacta somente a partida solicitada;
- usa cache para evitar releituras;
- mantém compatibilidade com os artefatos fragmentados usados no ambiente de
  desenvolvimento.

### Cálculo das métricas

`app/services/statsbomb_parser.py` concentra:

- leitura e classificação dos eventos;
- métricas de equipes e jogadores;
- minutos em campo;
- posições e macroposições;
- scores contextuais;
- índice de influência;
- preparação dos radares;
- leituras táticas automáticas.

### Geração dos artefatos

`app/services/dashboard_builder.py` e
`scripts/build_dashboard_data.py` pertencem ao pipeline de desenvolvimento.
Eles não são executados ao abrir uma partida.

## Visualizações

### Cabeçalho da partida

Apresenta:

- seleções e bandeiras;
- placar;
- técnicos;
- data;
- estádio;
- árbitro;
- gols e minutos;
- placar separado da disputa por pênaltis, quando houver.

### História do jogo

Resumo automático curto com leituras apoiadas em números, como:

- comparação de PPDA;
- volume de counterpress;
- criação por xA;
- influência dos jogadores;
- diferenças de progressão ou ameaça ofensiva.

### Visão geral da partida

Compara as duas equipes lado a lado. Entre as métricas disponíveis estão:

- xG;
- xA;
- finalizações;
- chutes no alvo;
- conversão de finalizações;
- passes;
- passes completos;
- precisão de passe;
- passes sob pressão;
- passes progressivos;
- conduções progressivas;
- distância percorrida em progressão;
- dribles;
- desarmes;
- ações defensivas;
- counterpress;
- PPDA.

As barras dessa seção são comparações internas da partida. Elas podem usar
escalas relativas aos dois times, mas não são a escala usada nos radares.

### Mapa de chutes

O mapa de chutes usa:

- círculo para uma finalização;
- estrela para um gol;
- tamanho do ponto proporcional ao xG;
- cor correspondente à equipe;
- menor opacidade para chutes sem gol.

Filtros disponíveis:

- equipe;
- jogador;
- período;
- todos os chutes;
- somente gols;
- somente chutes no alvo;
- somente xG alto.

Na visualização ampliada, o campo mostra o terço ofensivo em formato
panorâmico para facilitar a leitura das finalizações.

### Mapa de passes

O campo segue a convenção StatsBomb de `120 x 80`.

- verde: passe completo;
- vermelho: passe incompleto;
- seta: direção do passe;
- contorno branco: passe selecionado.

O mapa permite filtrar por:

- equipe;
- jogador;
- período.

No modo de passes, um jogador específico deve ser selecionado para evitar a
sobreposição ilegível de todos os passes da partida.

### Mapa de pênaltis

A aba é exibida quando a partida possui:

- pênalti durante o jogo; ou
- disputa por pênaltis.

O mapa diferencia:

- gol;
- defesa;
- erro;
- posição final da bola.

Eventos da disputa, identificados pelo período 5 da StatsBomb, não contaminam
o xG, os gols e as métricas do tempo normal.

### Fluxo de xG

Gráfico em degraus do xG acumulado ao longo da partida.

Cada finalização acrescenta seu `shot_statsbomb_xg` ao total da equipe:

```text
xG acumulado no minuto t =
    soma do xG de todos os chutes até o minuto t
```

### Momentum

Agrupa a partida em blocos de cinco minutos e permite alternar entre:

- xG;
- pressão;
- progressão;
- finalizações.

Para pressão, são considerados eventos de pressão e counterpress. Para
progressão, entram passes progressivos, conduções progressivas e recuperações
ofensivas.

### Mapa de pressão por equipe

Apresenta a densidade espacial dos eventos `Pressure`.

- áreas mais intensas indicam maior concentração de pressões;
- cada equipe possui seu próprio campo;
- as equipes são orientadas atacando da esquerda para a direita;
- a direção do ataque aparece abaixo do mapa.

O mapa informa onde a pressão ocorreu, não necessariamente onde a bola foi
recuperada.

### Construtores de jogo

Destaca jogadores com participação relevante em:

- xA;
- passes progressivos;
- passes para o terço final;
- passes para a área;
- criação de finalizações.

### Intensidade defensiva

Compara:

- quantidade de counterpress;
- PPDA aproximado.

As duas medidas possuem leituras diferentes:

- mais counterpress representa maior volume de pressão pós-perda;
- menor PPDA representa maior intensidade defensiva estimada.

### Progressões dos jogadores

Compara:

- passes progressivos;
- conduções progressivas;
- distância percorrida em progressão.

### Radares dos jogadores

A linha colorida representa o jogador naquela partida. A linha cinza representa
a média da macroposição na Copa.

Os radares não usam o maior valor da partida como referência. Eles usam a
distribuição do torneio por macroposição.

Macroposições:

- Goleiro;
- Zagueiro;
- Lateral/Ala;
- Volante/Meio-campista;
- Meia ofensivo/Ponta;
- Centroavante.

Dimensões de jogadores de linha:

- Ataque;
- Criação;
- Progressão;
- Passe;
- Defesa;
- Pressão.

Dimensões de goleiros:

- Defesa do gol;
- Jogo com os pés;
- Bolas longas;
- Ações fora da área;
- Pressão recebida;
- Participação na construção.

### Comparação de jogadores

A comparação simples mantém o radar específico de cada jogador.

A comparação ampliada:

- permite trocar os dois jogadores;
- usa dimensões gerais para comparar funções diferentes;
- lista métricas lado a lado;
- destaca o melhor valor em cada linha;
- diferencia total da partida, score contextual e influência;
- gera um resumo automático curto.

### Detalhe individual

Pode ser aberto ao clicar:

- em um radar;
- em uma linha da tabela de jogadores.

O modal apresenta:

- radar específico da função;
- média da macroposição;
- valores da partida;
- perfil contextual;
- diferença para a referência;
- mapa de ações do jogador.

## Métricas e cálculos

### Expected Goals — xG

O xG é fornecido pela StatsBomb em cada finalização:

```text
xG total = soma de shot_statsbomb_xg
```

O valor representa a probabilidade estimada de uma finalização resultar em
gol. O dashboard não treina um novo modelo de xG.

### Expected Assists — xA

O xA atribui ao passe que criou uma finalização o valor de xG daquele chute:

```text
xA do passe = xG da finalização criada
xA total = soma dos valores de xA
```

São relacionados os passes marcados como assistência para chute e as
finalizações correspondentes.

### Passe completo

Na StatsBomb, a ausência de `pass_outcome` representa um passe completo:

```text
passe completo =
    tipo do evento é Pass
    e pass_outcome está vazio
```

### Precisão de passe

```text
precisão de passe =
    passes completos / passes tentados × 100
```

### Passes sob pressão

São passes com `under_pressure` verdadeiro.

```text
precisão sob pressão =
    passes completos sob pressão
    / passes tentados sob pressão
    × 100
```

### Chutes no alvo

Resultados considerados no alvo:

```text
Goal
Saved
Saved to Post
```

### Conversão de finalizações

```text
conversão =
    gols / finalizações × 100
```

### Dribles, desarmes e duelos

As taxas de aproveitamento seguem:

```text
aproveitamento =
    ações bem-sucedidas / tentativas × 100
```

O mesmo princípio é aplicado a:

- dribles;
- desarmes;
- duelos;
- duelos aéreos;
- cruzamentos;
- passes longos.

Quando o denominador é zero, a métrica é exibida como `N/D`, acompanhada do
volume, por exemplo:

```text
75% (15/20)
```

### Passes progressivos

Um passe completo é classificado como progressivo quando:

- avança pelo menos 10 unidades no eixo longitudinal; ou
- começa antes de `x = 80` e termina no terço final, em `x >= 80`.

### Conduções progressivas

A mesma regra espacial é aplicada a eventos `Carry`:

- avanço longitudinal de pelo menos 10 unidades; ou
- entrada no terço final.

### Distância percorrida em progressão

Considera apenas o avanço longitudinal positivo:

```text
distância da ação =
    máximo(0, x final - x inicial)
```

```text
distância percorrida em progressão =
    distância dos passes progressivos
    + distância das conduções progressivas
```

### Entradas no terço final

```text
x inicial < 80
e x final >= 80
```

### Passes para a área

O destino do passe deve atender:

```text
x final >= 102
e 18 <= y final <= 62
```

### Counterpress

Conta eventos defensivos com a marcação `counterpress`, que identifica ações
de pressão imediatamente após a perda da posse.

```text
percentual de counterpress =
    counterpress / eventos de pressão × 100
```

### PPDA aproximado

```text
PPDA =
    passes permitidos ao adversário na zona analisada
    / ações defensivas
```

Quanto menor o PPDA, maior a intensidade defensiva estimada.

### Recuperações ofensivas

São recuperações bem-sucedidas em região avançada do campo, utilizadas nas
leituras de pressão e momentum.

### Minutos em campo

Os minutos são derivados dos intervalos das posições nas escalações, levando
em conta entradas, saídas e o fim efetivo da partida.

### Valores por 90 minutos

Valores por 90 são usados para construir referências comparáveis no torneio:

```text
valor por 90 =
    valor bruto / minutos jogados × 90
```

A interface principal mostra os totais produzidos naquela partida. O valor por
90 é utilizado principalmente na comparação estatística com a macroposição.

### Filtros mínimos de minutos

- radares e comparações contextuais: mínimo de 30 minutos;
- rankings principais: mínimo de 45 minutos;
- referência acumulada do torneio: mínimo de 90 minutos;
- tabela completa: mostra todos, sinalizando amostras pequenas.

### Score contextual de 0 a 100

Para cada métrica e macroposição, são calculados `p05` e `p95` usando a Copa
inteira:

```text
score =
    (valor por 90 - p05)
    / (p95 - p05)
    × 100
```

Regras:

- valores abaixo de 0 são limitados a 0;
- valores acima de 100 são limitados a 100;
- quando `p95 <= p05`, o resultado é 50.

Esse score responde:

> Como o jogador se saiu nesta partida em relação aos atletas da mesma função
> no torneio?

### Média cinza do radar

A referência cinza:

- usa a mesma escala contextual do jogador;
- representa a macroposição na Copa;
- é ponderada pelos minutos acumulados.

### Dimensões agregadas

Cada dimensão é uma média ponderada de scores individuais.

Exemplo da dimensão de progressão:

```text
Progressão =
    0,45 × score de passes progressivos
    + 0,35 × score de conduções progressivas
    + 0,20 × score de distância em progressão
```

Os pesos mudam conforme a macroposição:

- atacantes priorizam ataque e criação;
- meias e volantes priorizam passe, progressão, pressão e defesa;
- zagueiros priorizam defesa, passe e progressão;
- goleiros usam dimensões próprias.

### Perfil contextual

O perfil contextual é a combinação ponderada das dimensões do radar, apresentada
na escala:

```text
0 a 100
```

Ele deve ser lido como score relativo à função, não como percentual de acerto.

### Índice de influência

Influência é uma medida separada, com base 100:

```text
influência =
    score ponderado do jogador
    / score médio da macroposição
    × 100
```

Exemplos:

- `100`: média da macroposição;
- `130`: aproximadamente 30% acima da média;
- `80`: aproximadamente 20% abaixo da média.

Não se deve confundir:

- `86/100`: score contextual;
- `130,1`: índice de influência;
- `+30%`: diferença para a média da função.

## Dados e reconstrução analítica

O uso normal não exige os dados brutos. Para modificar fórmulas ou reconstruir
o banco, é necessário restaurar os JSONs da StatsBomb em `data/raw/`.

### Instalar dependências de desenvolvimento

```bash
uv sync --extra build
```

Esse grupo adiciona:

- pandas;
- PyArrow;
- StatsBombPy;
- Matplotlib;
- mplsoccer;
- seaborn.

### Reconstruir todas as partidas

```bash
uv run python scripts/build_dashboard_data.py --force
```

O pipeline:

1. lê os JSONs brutos;
2. calcula as referências do torneio;
3. gera artefatos intermediários;
4. calcula mapas, métricas e leituras;
5. cria novamente `data/dashboard.sqlite3`.

### Reconstruir uma partida

```bash
uv run python scripts/build_dashboard_data.py \
  --match-id 3857271 \
  --force
```

Uma reconstrução isolada atualiza os artefatos intermediários da partida. Para
reempacotar o banco completo depois:

```bash
uv run python scripts/build_dashboard_data.py --pack-only
```

### Empacotar sem recalcular

`--pack-only` lê os artefatos existentes em `data/processed/` e recria o banco
compacto:

```bash
uv run python scripts/build_dashboard_data.py --pack-only
```

Depois de substituir o banco, reinicie o Uvicorn para limpar o cache em
memória.

## Testes

### Ambiente compacto

```bash
uv run python -m unittest discover -s tests -q
```

Sem `data/raw/`, os testes de runtime e do banco compacto são executados. Os
testes que recalculam métricas a partir dos eventos brutos são ignorados.

### Ambiente analítico completo

Com `data/raw/` restaurado e as dependências de build instaladas:

```bash
uv sync --extra build
uv run python -m unittest discover -s tests -q
```

## Convenções importantes

- O campo StatsBomb possui coordenadas `120 x 80`.
- A origem espacial fica no canto superior esquerdo.
- O eixo `x` representa o comprimento do campo.
- O eixo `y` representa a largura.
- Eventos do período 5 representam disputa por pênaltis.
- A ausência de `pass_outcome` representa passe completo.
- A UI não recalcula métricas pesadas.
- O banco SQLite é a fonte principal do runtime.
- `data/raw/` e `data/processed/` são materiais opcionais de desenvolvimento e
  não fazem parte da distribuição compacta no Git.
