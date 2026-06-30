import asyncio
import os
from playwright.async_api import async_playwright
from app.services.vibra_crawler import VibraCrawlerService

async def debug_history():
    service = VibraCrawlerService()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("🔐 Fazendo login...")
        if not await service._login(page):
            print("❌ Falha no login")
            return
            
        # Vai para um orçamento específico (ex: 4842 -> Posto Mori)
        budget_id = "4842"
        url = f"https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement/BudgetDetail?BudgetId={budget_id}"
        print(f"🌐 Acessando {url}...")
        await page.goto(url, wait_until="networkidle")
        
        print("⏳ Aguardando carregamento do BOM...")
        try:
            # Espera até que a tabela tenha linhas de dados
            await page.wait_for_selector("table tbody tr", timeout=30000)
            print("✅ BOM carregado!")
        except:
            print("⚠️ Timeout aguardando BOM, prosseguindo assim mesmo...")
        
        # Clica no botão Histórico
        btn_hist = await page.query_selector("button:has-text('Histórico')")
        if btn_hist:
            print("🔘 Clicando no botão Histórico...")
            await btn_hist.click()
            await asyncio.sleep(10)
        
        print(f"Título da página: {await page.title()}")
        await page.screenshot(path="app/data/vibra/history_full_page.png", full_page=True)
        print("📸 Screenshot da página inteira salva em app/data/vibra/history_full_page.png")
        
        # Lista todos os elementos que podem ser o histórico
        print("🔍 Procurando elementos relacionados a histórico...")
        els = await page.query_selector_all(".osui-sidebar, .osui-sidebar-content, .osui-modal, [id*='history'], [class*='history']")
        for i, el in enumerate(els):
            print(f"  [{i}] Elemento: {await el.get_attribute('class')} | ID: {await el.get_attribute('id')}")
            text = await el.inner_text()
            print(f"      Texto: {text[:200]}...")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_history())
