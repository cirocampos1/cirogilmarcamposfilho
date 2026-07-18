import json

def fix_palette():
    path = r'G:\pythonProject\Aula_Cbf\analise-dados\02-analise-exploratoria\brasileirao_EDA copy.ipynb'
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            if 'cores_por_clube = {' in source:
                # Add dynamic fallback after the dictionary definition
                fallback_code = "\n# Fallback dinâmico para times novos/renomeados:\nfor clube in serie_a['Squad'].unique():\n    if clube not in cores_por_clube:\n        cores_por_clube[clube] = 'gray'\n"
                
                # We can just append this to the end of the cell
                source += fallback_code
                
                cell['source'] = [line + '\n' for line in source.split('\n')[:-1]]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

if __name__ == "__main__":
    fix_palette()
