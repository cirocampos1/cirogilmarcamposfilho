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
        await page.goto("https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement/ConstructionMonitoring")
        await page.fill("#Input_Username", os.getenv("VIBRA_USER"))
        await page.fill("#Input_Password", os.getenv("VIBRA_PASS"))
        await page.click("button.cs-login-btn")
        await page.wait_for_selector(".cs-table", timeout=60000)
        
        print("🔍 Capturando URLs de rede na página de Detalhe do Orçamento...")
        
        async def handle_response(response):
            if "DataAction" in response.url:
                print(f"URL: {response.url}")
                try:
                    # Tenta ver se tem a palavra 'Category' ou 'Product' no corpo
                    body = await response.text()
                    if "Category" in body or "Product" in body or "Quantity" in body:
                        print(f"  ⭐ POSSÍVEL BOM ENCONTRADA: {response.url}")
                except: pass

        page.on("response", handle_response)
        
        # Tenta entrar no orçamento 1125 (que vimos no seu print)
        await page.goto("https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement/BudgetDetail?BudgetId=1125")
        await page.wait_for_timeout(10000)
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
