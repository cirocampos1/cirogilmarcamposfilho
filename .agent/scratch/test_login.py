import asyncio
import os
from playwright.async_api import async_playwright
from app.services.vibra_crawler import VibraCrawlerService

async def test():
    print("🚀 Iniciando teste de login...")
    crawler = VibraCrawlerService()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            success = await crawler._login(page)
            print(f"✅ Resultado do Login: {success}")
            if success:
                print(f"📍 URL Atual: {page.url}")
        except Exception as e:
            print(f"❌ Erro durante o teste: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(test())
