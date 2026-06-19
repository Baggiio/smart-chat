from fastapi import FastAPI

from app.routers.chat import router as chat_router

app = FastAPI(
    title="Smart Chat API",
    version="0.1.0"
)

app.include_router(chat_router)

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}