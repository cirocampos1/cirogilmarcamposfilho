import asyncio
from app.clients.sankhya.gateway_client import SankhyaGatewayClient
from app.clients.sankhya.token_provider import SankhyaTokenProvider
from app.repositories.sankhya_dbexplorer_repository import SankhyaDbExplorerRepository

async def main():
    token_provider = SankhyaTokenProvider()
    gateway = SankhyaGatewayClient(token_provider)
    db = SankhyaDbExplorerRepository(gateway)
    
    print("--- TESTE JOIN TCSPRJ ---")
    sql = """
    SELECT TOP 5
        S.CODPROJ,
        P.ABREVIATURA,
        P.CODCLT,
        ISNULL(C.NOMEPARC, 'SEM CLIENTE') as NOMEPARC
    FROM sankhya.AD_SINAL_SHEET S
    LEFT JOIN sankhya.TCSPRJ P ON S.CODPROJ = P.CODPROJ
    LEFT JOIN sankhya.TGFPAR C ON P.CODCLT = C.CODPARC
    """
    try:
        res = await db.execute_query(sql)
        rows = db.to_rows(res)
        for r in rows:
            print(f"Proj: {r['CODPROJ']} | Nome: {r['ABREVIATURA']} | Cliente: {r['NOMEPARC']}")
    except Exception as e:
        print(f"ERRO: {e}")

if __name__ == "__main__":
    asyncio.run(main())
