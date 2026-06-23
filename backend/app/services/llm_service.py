from functools import lru_cache
from langchain_openai import ChatOpenAI
from app.core.config import get_settings

SYSTEM_PROMPT = """
Você é o assistente virtual do Smart Chat.

Responda de maneira clara, objetiva e didática.
Não invente informações quando não souber a resposta.
""".strip()

@lru_cache
def get_chat_model() -> ChatOpenAI:
    settings = get_settings()

    return ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key.get_secret_value(),
        timeout=30,
        max_retries=2
    )

async def generate_assistant_response(history: list[tuple[str, str]], content: str) -> str:
    messages = [("system", SYSTEM_PROMPT), *history, ("human", content)]

    response = await get_chat_model().ainvoke(messages)

    return response.text.strip()

