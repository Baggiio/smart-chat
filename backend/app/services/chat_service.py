from app.services.agent_service import generate_agent_response
from app.schemas.chat import MessageResponse
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

    history = [("human" if message.role == "user" else "ai", message.content) for message in _messages]

    assistant_content = await generate_agent_response(history=history, content=content)

    assistant_message = MessageResponse(
        id=str(uuid4()),
        role="assistant",
        content=assistant_content,
        createdAt=datetime.now(timezone.utc)
    )

    _messages.extend([user_message, assistant_message])

    return assistant_message

