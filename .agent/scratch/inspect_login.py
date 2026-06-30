import asyncio
from playwright.async_api import async_playwright

async def inspect():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://vibraenergiasa.outsystemsenterprise.com/ConstructionManagement/Budgets')
        await page.wait_for_timeout(5000)
        
        print("--- INPUTS ---")
        inputs = await page.query_selector_all('input')
        for i in inputs:
            iid = await i.get_attribute('id')
            iname = await i.get_attribute('name')
            iplaceholder = await i.get_attribute('placeholder')
            itype = await i.get_attribute('type')
            print(f"ID: {iid} | Name: {iname} | Type: {itype} | Placeholder: {iplaceholder}")
            
        print("--- BUTTONS ---")
        buttons = await page.query_selector_all('button')
        for b in buttons:
            bid = await b.get_attribute('id')
            btext = await b.inner_text()
            print(f"ID: {bid} | Text: {btext}")
            
        await page.screenshot(path="debug_inspect_login.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(inspect())
