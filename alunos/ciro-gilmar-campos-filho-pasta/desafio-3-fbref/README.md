# Desafio 3: Web Scraping com FBref e SoccerData

Bem-vindo ao terceiro desafio do bootcamp! Desta vez, vamos aprofundar nossos conhecimentos em **Engenharia de Dados** e extração resiliente de dados (Web Scraping) no ecossistema do futebol.

## Objetivo
O site **FBref.com** é uma das fontes de dados mais ricas sobre futebol no mundo. No entanto, ele possui regras de segurança rígidas contra automação (banimento rápido de IPs se você não for cuidadoso). 

Seu objetivo é utilizar o pacote [`soccerdata`](https://soccerdata.readthedocs.io/), que simplifica a coleta e já lida com o caching automático das páginas, para montar uma base de dados completa do Brasileirão Série A e realizar análises exploratórias.

## Estrutura do Projeto

* `src/fbref_extract.py`: Script principal que consome os métodos da classe `sd.FBref()` para extrair tabela, resultados, e estatísticas de times/jogadores.
* `data/parquet/`: Pasta onde os DataFrames são salvos em formato analítico `Parquet`.
* `data/fbref_brasileirao.db`: Banco de dados SQLite criado automaticamente com as tabelas do campeonato.

## Instruções (Para o Aluno)

1. **Instale as dependências:**
   Este projeto utiliza o `uv` para gestão de pacotes rápidos.
   ```bash
   uv sync
   # ou instale manualmente:
   # uv add soccerdata pandas pyarrow
   ```

2. **Execute o Extrator:**
   Navegue até a raiz da pasta e execute o script. 
   > **Aviso:** A primeira vez que você rodar, o pacote fará downloads do site e aplicará sleeps automáticos. Se der erro de *Too Many Requests (HTTP 429)*, pare e espere um tempo. O cache local te salva de recomeçar do zero!
   ```bash
   uv run src/fbref_extract.py
   ```

3. **Explore e Crie!**
   Com o SQLite e Parquet preenchidos em `data/`, crie um arquivo Jupyter Notebook (`notebooks/exploracao.ipynb`) e cruze a tabela de jogadores para ver:
   * Qual o jogador com o melhor xG (Expected Goals) por 90 minutos?
   * Qual equipe mais cede chutes aos adversários?

Boa sorte e boas raspagens de dados! ⚽
