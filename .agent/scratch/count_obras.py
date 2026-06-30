import asyncio
import os
import sys

# Add current directory to path
sys.path.append(os.getcwd())

from app.routers.vibra import _get_vibra_repo

async def main():
    repo = _get_vibra_repo()
    obras = await repo.get_obras()
    print(f"Total Obras no Banco: {len(obras)}")

if __name__ == "__main__":
    asyncio.run(main())
