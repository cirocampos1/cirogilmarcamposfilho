
import json
import pandas as pd

def analyze():
    # Load Excel
    df = pd.read_excel('mitra_dre/5137.xlsx')
    
    # Load JSON Hierarchy
    with open('app/data/performance_dre_hierarchy_structured.json', 'r') as f:
        hierarchy = json.load(f)
    
    # Compare labels and levels
    print("INDEX | INDENT (LVL) | JSON LABEL | EXCEL LABEL | JAN VALUE")
    print("-" * 80)
    for i in range(len(hierarchy)):
        json_item = hierarchy[i]
        excel_label = df.iloc[i, 0] if i < len(df) else "N/A"
        excel_val = df.iloc[i, 4] if i < len(df) else "N/A"
        
        # Check if they match
        match = "✓" if str(json_item['label']).strip().upper() == str(excel_label).strip().upper() else "✗"
        
        print(f"{i:5} | {json_item['level']:<10} | {json_item['label']:<20} | {str(excel_label)[:20]:<20} | {excel_val} {match}")
        
        if i > 150: break

if __name__ == "__main__":
    analyze()
