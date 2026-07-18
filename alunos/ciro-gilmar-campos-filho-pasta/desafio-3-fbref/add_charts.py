import json
import warnings

# Script para adicionar células gráficas no Notebook existente
def add_charts():
    with open('notebooks/exploracao.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    new_cells = [
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "---\n",
        "## 3. Visualizações de Dados 📊\n",
        "\n",
        "Agora vamos explorar visualmente os dados coletados criando diversos gráficos usando `matplotlib` e `seaborn`."
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "# Configurando o estilo visual dos gráficos\n",
        "sns.set_theme(style=\"whitegrid\")\n",
        "plt.rcParams['figure.figsize'] = (10, 6)"
       ]
      },
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "### Gráfico 1: Top 10 Artilheiros por 90 Minutos\n",
        "Mostra de forma ranqueada quem são os matadores da liga em proporção ao tempo jogado."
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "plt.figure(figsize=(10, 6))\n",
        "sns.barplot(data=top_xg.head(10), x=col_xg90, y=col_player, palette=\"viridis\")\n",
        "plt.title(\"Top 10 Jogadores: Gols por 90 Minutos\", fontsize=14)\n",
        "plt.xlabel(\"Gols p/ 90 min\", fontsize=12)\n",
        "plt.ylabel(\"Jogador\", fontsize=12)\n",
        "plt.show()"
       ]
      },
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "### Gráfico 2: Gols vs Assistências (Visão Geral de Playmakers)\n",
        "Quem participa mais ativamente em gols? (Apenas quem tem minutos consideráveis)"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "col_ast = ('Performance', 'Ast')\n",
        "col_gls = ('Performance', 'Gls')\n",
        "\n",
        "# Filtramos para ver apenas jogadores com pelo menos 1 gol ou 1 assistência\n",
        "df_playmakers = df_filtered[(df_filtered[col_gls] > 0) | (df_filtered[col_ast] > 0)]\n",
        "\n",
        "plt.figure(figsize=(10, 8))\n",
        "sns.scatterplot(data=df_playmakers, x=col_gls, y=col_ast, hue=col_team, s=100, alpha=0.7, legend=False)\n",
        "plt.title(\"Gols x Assistências (Total na Temporada)\", fontsize=14)\n",
        "plt.xlabel(\"Gols Marcados\", fontsize=12)\n",
        "plt.ylabel(\"Assistências\", fontsize=12)\n",
        "\n",
        "# Adicionar rótulos para os jogadores muito acima da média\n",
        "for i in range(df_playmakers.shape[0]):\n",
        "    gls = df_playmakers[col_gls].iloc[i]\n",
        "    ast = df_playmakers[col_ast].iloc[i]\n",
        "    if gls > 5 or ast > 5:\n",
        "        plt.text(gls + 0.2, ast, df_playmakers[col_player].iloc[i], fontsize=9)\n",
        "\n",
        "plt.show()"
       ]
      },
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "### Gráfico 3: Distribuição de Idades na Série A\n",
        "Como é o perfil de idade dos jogadores atuando ativamente no campeonato?"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "col_age = ('age', '')\n",
        "# A idade vem como string ex: '25-143', vamos separar pelo hífen e pegar só o ano\n",
        "df_filtered['Idade'] = df_filtered[col_age].str.split('-').str[0].astype(float)\n",
        "\n",
        "plt.figure(figsize=(10, 5))\n",
        "sns.histplot(data=df_filtered, x='Idade', bins=15, kde=True, color=\"#1f77b4\")\n",
        "plt.title(\"Distribuição de Idades dos Jogadores (Mín 500 min jogados)\", fontsize=14)\n",
        "plt.xlabel(\"Idade\", fontsize=12)\n",
        "plt.ylabel(\"Quantidade de Jogadores\", fontsize=12)\n",
        "plt.show()"
       ]
      },
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "### Gráfico 4: Piores Defesas (Gols Sofridos por Equipe)\n",
        "Visualizando os dados que calculamos na parte 2."
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "plt.figure(figsize=(10, 8))\n",
        "sns.barplot(data=df_defense, x='goals_conceded', y='team', palette=\"Reds_r\")\n",
        "plt.title(\"Total de Gols Sofridos por Equipe\", fontsize=14)\n",
        "plt.xlabel(\"Gols Sofridos\", fontsize=12)\n",
        "plt.ylabel(\"Equipe\", fontsize=12)\n",
        "plt.show()"
       ]
      }
    ]

    nb['cells'].extend(new_cells)

    with open('notebooks/exploracao.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

if __name__ == '__main__':
    add_charts()
