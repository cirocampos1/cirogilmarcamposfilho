import asyncio
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def test_manual_xml():
    db = SankhyaDbExplorerRepository(SankhyaGatewayClient(SankhyaTokenProvider()))
    
    # XML Minimalista para a obra 4836
    xml = """
    <obras>
        <obra>
            <id_portal>4836</id_portal>
            <cliente>TESTE SYNC</cliente>
            <status_obra>Sincronizando...</status_obra>
            <status_montagem>TESTE_MONT</status_montagem>
            <json_full>{"teste": true}</json_full>
        </obra>
    </obras>
    """
    
    print("Enviando XML manual para a SP...")
    try:
        resp = await db.execute_stored_procedure("sankhya.AD_STP_VIBRA_SYNC_BATCH", {
            "P_XML_BATCH": xml
        })
        print("Resposta do Sankhya:", resp)
    except Exception as e:
        print("Erro na SP:", e)

if __name__ == "__main__":
    asyncio.run(test_manual_xml())
