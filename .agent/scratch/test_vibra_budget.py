import asyncio
import logging
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("test_vibra")

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

async def test_budget_pagination():
    user = os.getenv("VIBRA_USER")
    password = os.getenv("VIBRA_PASS")
    base_url = "https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        async def handle_response(response):
            if "DataAction" in response.url:
                logger.info(f"📡 API Interceptada: {response.url.split('/')[-1]}")
                try:
                    body = await response.text()
                    if "Budget" in response.url:
                        data = json.loads(body)
                        # Tenta vários caminhos possíveis
                        items = data.get("data", {}).get("BudgetListStrucRetur", {}).get("List", [])
                        if not items:
                            items = data.get("data", {}).get("List", [])
                        
                        logger.info(f"📦 Itens encontrados na resposta: {len(items)}")
                        for it in items:
                            id_val = it.get("Id") or it.get("BudgetID")
                            if id_val not in [b.get("Id") for b in budgets_data]:
                                budgets_data.append({"Id": id_val, "data": it})
                except Exception as e:
                    logger.error(f"Erro ao ler body: {e}")

        budgets_data = []
        page.on("response", handle_response)

        logger.info("🔐 Fazendo login...")
        await page.goto(f"{base_url}/Budgets")
        if await page.query_selector("#Input_Username"):
            await page.fill("#Input_Username", user)
            await page.fill("#Input_Password", password)
            await page.click("button.cs-login-btn")
        
        await page.wait_for_selector("tr.cs-row-table, .cs-table", timeout=60000)
        await page.wait_for_timeout(5000)
        logger.info(f"Página 1: {len(budgets_data)} orçamentos acumulados")

        next_btn = await page.query_selector("button.pagination-button[aria-label*='seguinte']:not([disabled])")
        if next_btn:
            logger.info("⏭️ Clicando em Próximo...")
            await next_btn.click()
            await page.wait_for_timeout(8000)
            logger.info(f"Total acumulado: {len(budgets_data)} orçamentos")
        else:
            logger.info("Botão 'Próximo' não encontrado ou desabilitado.")

        await browser.close()
        print(f"\nRESULTADO FINAL: {len(budgets_data)} orçamentos encontrados.")

if __name__ == "__main__":
    asyncio.run(test_budget_pagination())
