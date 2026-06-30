import os
import zipfile
import shutil
import pandas as pd

def clean_and_read(file_path):
    temp_dir = "temp_view"
    if os.path.exists(temp_dir): shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    style_path = os.path.join(temp_dir, "xl", "styles.xml")
    if os.path.exists(style_path):
        os.remove(style_path)
        with open(style_path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"></styleSheet>')
    fixed = "fixed_view.xlsx"
    with zipfile.ZipFile(fixed, 'w') as zip_ref:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, temp_dir)
                zip_ref.write(full_path, rel_path)
    shutil.rmtree(temp_dir)
    df = pd.read_excel(fixed)
    print(df.head(5).to_dict())
    if os.path.exists(fixed): os.remove(fixed)

if __name__ == "__main__":
    clean_and_read("docs/vibra/samples/Relatorio_de_orcamentos_02052026.xlsx")
