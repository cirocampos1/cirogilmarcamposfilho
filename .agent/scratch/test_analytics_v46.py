import asyncio
import json
from app.services.vibra_analytics import VibraAnalyticsService

async def test_analytics():
    print("🧪 Testando Analytics com dados v4.6...")
    try:
        with open("app/data/vibra/latest_sync.json", "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        analytics = VibraAnalyticsService()
        dashboard = await analytics.analyze(raw_data)
        
        print(f"✅ Sucesso! Assessments gerados: {len(dashboard.assessments)}")
        print(f"✅ Previsão de Fábrica gerada: {len(dashboard.production_forecast)} categorias")
        
    except Exception as e:
        import traceback
        print(f"❌ FALHA NO ANALYTICS: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_analytics())
