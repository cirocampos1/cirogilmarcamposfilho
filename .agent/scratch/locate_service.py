import sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    from app.services.vibra_crawler import VibraCrawlerService
    import inspect
    print(f"VibraCrawlerService file: {inspect.getfile(VibraCrawlerService)}")
    sig = inspect.signature(VibraCrawlerService.run_full_sync)
    print(f"run_full_sync signature: {sig}")
except Exception as e:
    print(f"Error: {e}")
