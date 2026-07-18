import json
import os

NOTEBOOK_PATH = r"G:\pythonProject\Aula_Cbf\analise-dados\02-analise-exploratoria\brasileirao_EDA copy.ipynb"

def modify_notebook():
    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # We want to replace the first few cells that deal with selenium scraping and CSV loading
    # Let's keep the very first cell (imports) and then replace up to the merge cell
    
    # Let's inspect the cells
    first_import_cell = nb['cells'][0]
    
    # We will construct a new list of cells
    new_cells = [first_import_cell]
    
    # Add a markdown cell explaining the change
    new_cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Carregamento dos Dados via Parquet (SoccerData)\n",
            "Nesta vers\u00e3o, substitui\u00edmos a raspagem via Selenium/Tor pelo uso dos dados parquet gerados previamente pelo nosso script `fbref_extract.py` usando `soccerdata`."
        ]
    })
    
    # Add code cell to load parquet
    new_cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "\n",
            "parquet_path = r'G:\\pythonProject\\Aula_Cbf\\desafio-3-fbref\\data\\parquet\\player_stats.parquet'\n",
            "df_parquet = pd.read_parquet(parquet_path).reset_index()\n",
            "\n",
            "def clean_fbref_cols(df: pd.DataFrame) -> pd.DataFrame:\n",
            "    if not isinstance(df.columns, pd.MultiIndex):\n",
            "        return df\n",
            "\n",
            "    new_cols = []\n",
            "    for col in df.columns:\n",
            "        g = str(col[0]).strip()\n",
            "        name = str(col[1]).strip() if len(col) > 1 else g\n",
            "        if g == \"Per 90 Minutes\":\n",
            "            name = f\"{name}_90\"\n",
            "        if name == \"\":\n",
            "            name = g\n",
            "        new_cols.append(name)\n",
            "    df = df.copy()\n",
            "    df.columns = new_cols\n",
            "    return df\n",
            "\n",
            "df_combined = clean_fbref_cols(df_parquet)\n",
            "\n",
            "# Renomeando as colunas de \u00edndice para bater com o notebook original\n",
            "renames = {\n",
            "    'player': 'Player',\n",
            "    'team': 'Squad',\n",
            "    'nation': 'Nation',\n",
            "    'pos': 'Pos',\n",
            "    'age': 'Age',\n",
            "    'born': 'Born',\n",
            "    'MP': 'MP',\n",
            "    'Starts': 'Starts',\n",
            "    'Min': 'Min',\n",
            "    '90s': '90s'\n",
            "}\n",
            "df_combined = df_combined.rename(columns=renames)\n",
            "display(df_combined.head(3))"
        ]
    })
    
    # Now find the first cell in the original notebook that comes AFTER the merging block
    # In the original, the merge block created `df_combined = df_combined[meta_cols + other_cols]`
    # We will search for a cell that is markdown or code and does NOT contain selenium/tor/merge logic
    
    skip = True
    for cell in nb['cells'][1:]:
        source = "".join(cell.get('source', []))
        if skip:
            # We look for the cell that prints info about df_combined, or the first EDA cell
            if "df_combined.info()" in source or "df_combined.head()" in source or "Análise Exploratória" in source or "analise exploratoria" in source.lower() or "limpeza" in source.lower():
                skip = False
                
            # If we see the cell right after the merge block, usually it's df_combined.info() or similar
            if "df_combined.shape" in source or "df_combined.describe()" in source or "duplicated()" in source:
                skip = False
                
        if not skip:
            new_cells.append(cell)
            
    nb['cells'] = new_cells
    
    with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        
if __name__ == '__main__':
    modify_notebook()
