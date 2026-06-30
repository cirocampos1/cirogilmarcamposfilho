import asyncio
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider

async def explore():
    try:
        tp = SankhyaTokenProvider()
        gw = SankhyaGatewayClient(tp)
        db = SankhyaDbExplorerRepository(gw)
        
        print("🔍 Explorando AD_SS_PEDIDOS...")
        res = await db.execute_query("SELECT TOP 1 * FROM sankhya.AD_SS_PEDIDOS")
        if res.get("rows"):
            print("✅ Colunas encontradas:")
            for col in res["rows"][0].keys():
                print(f"   - {col}")
        else:
            print("❌ Nenhuma linha encontrada em AD_SS_PEDIDOS")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    asyncio.run(explore())
