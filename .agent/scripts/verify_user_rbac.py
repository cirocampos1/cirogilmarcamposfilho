import asyncio
import argparse
import sys
import os

# Ajustar PYTHONPATH para encontrar os módulos do app
sys.path.append(os.getcwd())

from app.dependencies.sankhya import get_priorizacao_admin_service
from app.core.access import can_manage_sinalsheet

async def verify_user(username: str):
    print(f"--- Verificando RBAC para: {username} ---")
    
    service = get_priorizacao_admin_service()
    
    # 1. Carregar flags do banco
    try:
        flags = await service.get_manage_flags(username)
        print(f"Flags no Banco de Dados: {flags}")
        
        # 2. Simular payload de usuário
        user_payload = {
            "username": username,
            "manage_area_permissions": flags
        }
        
        # 3. Testar função de acesso
        has_access = can_manage_sinalsheet(user_payload)
        print(f"Resultado can_manage_sinalsheet: {'✅ ACESSO CONCEDIDO' if has_access else '❌ ACESSO NEGADO'}")
        
        if not has_access:
            print("\nPossíveis causas:")
            print("- A flag 'SS_GESTAO' está False no payload.")
            print("- O usuário não é admin e não está nas listas do .env.")
            
    except Exception as e:
        print(f"❌ Erro ao consultar banco: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True, help="Username LDAP/Sankhya")
    args = parser.parse_args()
    
    asyncio.run(verify_user(args.user))
