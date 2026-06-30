import asyncio
from app.services.vibra_crawler import VibraCrawlerService

async def test():
    crawler = VibraCrawlerService()
    try:
        # Tenta chamar com pages para ver se falha
        print("Testando chamada com pages=1...")
        # Mocking run_full_sync to not actually run playwright if possible, 
        # but here we just want to check the signature.
        # Actually, just checking the signature is enough.
        import inspect
        sig = inspect.signature(crawler.run_full_sync)
        print(f"Assinatura: {sig}")
        if 'pages' in sig.parameters:
            print("✅ 'pages' está na assinatura.")
        else:
            print("❌ 'pages' NÃO está na assinatura.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    asyncio.run(test())
