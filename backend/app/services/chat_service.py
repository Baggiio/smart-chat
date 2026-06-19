import asyncio
from datetime import datetime, timezone
from uuid import uuid4

from app.schemas.chat import MessageResponse

_messages: list[MessageResponse] = [
    MessageResponse(
        id=str(uuid4()),
        role="assistant",
        content="Olá! Sou seu assistente virtual. Como posso ajudar?",
        createdAt=datetime.now(timezone.utc)
    )
]

def get_messages() -> list[MessageResponse]:
    return list(_messages)

async def send_message(content: str) -> MessageResponse:
    user_message = MessageResponse(
        id=str(uuid4()),
        role="user",
        content=content,
        createdAt=datetime.now(timezone.utc)
    )

    _messages.append(user_message)

    await asyncio.sleep(0.8)

    assistant_message = MessageResponse(
        id=str(uuid4()),
        role="assistant",
        content=(
            f'Você disse: "{content}".'
            "Em breve essa resposta será gerada com LangChain."
        ),
        createdAt=datetime.now(timezone.utc)
    )

    _messages.append(assistant_message)

    return assistant_message

