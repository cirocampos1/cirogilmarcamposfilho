"""
Teste cirúrgico: verifica se o DbExplorerSP executa DML inline
após um SELECT bypass, ou se ignora tudo depois do primeiro statement.
"""
import asyncio
import json
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def test_inline_update():
    db = SankhyaDbExplorerRepository(SankhyaGatewayClient(SankhyaTokenProvider()))
    
    # Teste 1: bypass + UPDATE inline (sem SP)
    print("=== TESTE 1: SELECT bypass + UPDATE inline ===")
    sql_bypass_update = """
    SELECT 'BYPASS' AS STATUS;
    UPDATE sankhya.AD_VIBRA_OBRAS SET STATUS_MONT = 'INLINE_TEST' WHERE ID_PORTAL = 4836;
    """
    try:
        resp = await db.execute_query(sql_bypass_update)
        print("Resposta:", json.dumps(resp, indent=2, default=str))
    except Exception as e:
        print("Erro:", e)
    
    # Verificar se bateu
    print("\n=== VERIFICAÇÃO ===")
    check = await db.execute_query(
        "SELECT ID_PORTAL, STATUS_MONT, DT_ULT_SYNC FROM sankhya.AD_VIBRA_OBRAS WHERE ID_PORTAL = 4836"
    )
    rows = db.to_rows(check)
    print(json.dumps(rows, indent=2, default=str))

if __name__ == "__main__":
    asyncio.run(test_inline_update())
