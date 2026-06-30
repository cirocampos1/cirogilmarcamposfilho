from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.api.routes import router

app = FastAPI(title="SofaScore Player Dashboard", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.responses import RedirectResponse

FRONTEND_DIR = Path(__file__).parent / "frontend"
app.mount("/dashboard", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")

@app.get("/")
def root():
    return RedirectResponse(url="/dashboard")

app.include_router(router, prefix="")
