from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.chat import router as chat_router

app = FastAPI(
    title="Smart Chat API",
    version="0.1.0"
)

allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"]
)

app.include_router(chat_router)

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}