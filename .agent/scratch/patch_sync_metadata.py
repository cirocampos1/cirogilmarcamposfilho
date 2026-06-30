import os
import zipfile
import shutil
import pandas as pd
import json

def clean_excel(file_path):
    temp_dir = "temp_excel_fix_patch"
    if os.path.exists(temp_dir): shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    style_path = os.path.join(temp_dir, "xl", "styles.xml")
    if os.path.exists(style_path):
        os.remove(style_path)
        with open(style_path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"></styleSheet>')
    fixed_file = "fixed_report_patch.xlsx"
    with zipfile.ZipFile(fixed_file, 'w') as zip_ref:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, temp_dir)
                zip_ref.write(full_path, rel_path)
    shutil.rmtree(temp_dir)
    return fixed_file

def update_sync():
    excel_path = "docs/vibra/samples/Relatorio_de_orcamentos_02052026.xlsx"
    sync_path = "app/data/vibra/latest_sync.json"
    
    fixed_excel = clean_excel(excel_path)
    
    # Busca dinâmica da linha de cabeçalho
    df_raw = pd.read_excel(fixed_excel, header=None)
    header_row_idx = 0
    for i, row in df_raw.iterrows():
        if "ID DO ORÇAMENTO" in [str(v).upper() for v in row.values]:
            header_row_idx = i
            break
    
    print(f"Header encontrado na linha: {header_row_idx}")
    df = pd.read_excel(fixed_excel, header=header_row_idx)
    # Remove colunas vazias iniciais
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    metadata = {}
    for _, row in df.iterrows():
        # Limpeza do ID
        bid_raw = str(row.get("ID DO ORÇAMENTO", "")).strip()
        if not bid_raw or bid_raw == "nan": continue
        bid = bid_raw.split(".")[0]
        
        metadata[bid] = {
            "sap": str(row.get("CÓDIGO SAP", "")).strip(),
            "cnpj": str(row.get("CNPJ DO CLIENTE", "")).strip(),
            "cidade": str(row.get("CIDADE DO CLIENTE", "")).strip(),
            "uf": str(row.get("ESTADO DO CLIENTE", "")).strip(),
            "endereco": f"{row.get('ENDEREÇO DO CLIENTE', '')}, {row.get('CIDADE DO CLIENTE', '')}",
            "engenheiro": str(row.get("ENGENHEIRO RESPONSÁVEL", "")).strip(),
            "imposto": str(row.get("VALOR DA PARCELA DE IMPOSTO", "0")),
        }
    
    print(f"Metadados extraídos para {len(metadata)} orçamentos.")

    if os.path.exists(sync_path):
        with open(sync_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        upd_m, upd_b = 0, 0
        for item in data.get("monitoring", []):
            bid = str(item.get("id_portal", "")).split(".")[0]
            if bid in metadata:
                m = metadata[bid]
                item.update(m)
                item["engenheiro"] = m["engenheiro"].replace("Engenheiro responsável\n", "").strip()
                if "full_data" not in item: item["full_data"] = {}
                item["full_data"]["header"] = m
                upd_m += 1

        for b in data.get("budgets", []):
            bid = str(b.get("BudgetId", "")).split(".")[0]
            if bid in metadata:
                m = metadata[bid]
                b.update(m)
                b["engenheiro"] = m["engenheiro"].replace("Engenheiro responsável\n", "").strip()
                if "full_data" not in b: b["full_data"] = {}
                b["full_data"]["header"] = m
                upd_b += 1

        with open(sync_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"latest_sync.json atualizado: {upd_m} monitoramentos, {upd_b} orçamentos.")
    
    if os.path.exists(fixed_excel): os.remove(fixed_excel)

if __name__ == "__main__":
    update_sync()
