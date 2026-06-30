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
        
        await page.wait_for_timeout(10000)
        print(f"📍 URL após login: {page.url}")
        
        # Tenta forçar Budgets se não estiver lá
        if "/Budgets" not in page.url:
            print("📑 Redirecionando para /Budgets...")
            await page.goto("https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement/Budgets")
            await page.wait_for_timeout(5000)
        
        print("📸 Tirando screenshot...")
        await page.screenshot(path="app/data/vibra/debug_budgets.png", full_page=True)
        print(f"✅ Screenshot salva em app/data/vibra/debug_budgets.png. URL Final: {page.url}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
