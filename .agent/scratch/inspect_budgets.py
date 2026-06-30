import asyncio
import os
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("🔐 Fazendo login...")
        await page.goto("https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement/Budgets")
        await page.fill("#Input_Username", os.getenv("VIBRA_USER"))
        await page.fill("#Input_Password", os.getenv("VIBRA_PASS"))
        await page.click("button.cs-login-btn")
        
        print("⏳ Aguardando tabela de orçamentos...")
        await page.wait_for_selector(".cs-table, tr.cs-row-table", timeout=60000)
        
        print("🔍 Analisando estrutura da tabela...")
        rows = await page.query_selector_all("tr.cs-row-table")
        print(f"Encontradas {len(rows)} linhas na tabela.")
        
        if rows:
            # Pega o texto da primeira linha para ver os campos
            first_row = await rows[0].inner_text()
            print(f"Exemplo de linha: {first_row.replace('\n', ' | ')}")
            
            # Tenta pegar atributos data-header
            cells = await rows[0].query_selector_all("td")
            for cell in cells:
                header = await cell.get_attribute("data-header")
                text = await cell.inner_text()
                print(f"  Col: {header} | Valor: {text.strip()}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
