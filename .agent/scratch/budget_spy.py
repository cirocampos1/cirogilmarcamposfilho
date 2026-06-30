import asyncio
import os
import json
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto("https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement/Budgets")
        # Login se necessário
        if await page.query_selector("#Input_Username"):
            await page.fill("#Input_Username", os.getenv("VIBRA_USER"))
            await page.fill("#Input_Password", os.getenv("VIBRA_PASS"))
            await page.click("button.cs-login-btn")
            await page.wait_for_selector(".cs-table, tr.cs-row-table", timeout=60000)

        print("🕵️ Espionando chamadas de rede na página de Orçamentos...")
        
        async def handle_response(response):
            if "DataAction" in response.url:
                print(f"📡 CHAMADA DETECTADA: {response.url}")
                try:
                    body = await response.text()
                    if "Budget" in body:
                        print("  ✅ ESTA CHAMADA CONTÉM DADOS DE ORÇAMENTO!")
                except: pass

        page.on("response", handle_response)
        await page.goto("https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement/Budgets")
        await page.wait_for_timeout(10000)
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
