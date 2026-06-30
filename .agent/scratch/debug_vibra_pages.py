import asyncio
from playwright.async_api import async_playwright
import os
import sys
from pathlib import Path

# Adiciona o diretório atual ao path para importar app
sys.path.append(os.getcwd())

from app.services.vibra_crawler import VibraCrawlerService

async def debug_pages():
    service = VibraCrawlerService()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("🔐 Tentando login para debug...")
        if await service._login(page):
            print("📸 Capturando /Budgets...")
            await page.goto(f"{service.base_url}/Budgets")
            await page.wait_for_timeout(10000)
            await page.screenshot(path="debug_budgets_page.png")
            
            print("📸 Capturando /ConstructionMonitoring...")
            await page.goto(f"{service.base_url}/ConstructionMonitoring")
            await page.wait_for_timeout(10000)
            await page.screenshot(path="debug_monitoring_page.png")
            
            # Tenta um detalhe se soubermos um ID (ex: 1125)
            print("📸 Capturando /BudgetDetail?BudgetId=1125...")
            await page.goto(f"{service.base_url}/BudgetDetail?BudgetId=1125")
            await page.wait_for_timeout(10000)
            await page.screenshot(path="debug_detail_1125.png")
        else:
            print("❌ Falha no login durante debug.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_pages())
