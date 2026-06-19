from fastapi import APIRouter, status

from app.schemas.chat import MessageCreate, MessageResponse
from app.services.chat_service import get_messages, send_message

router = APIRouter(
    prefix="/api/messages",
    tags=["messages"]
)

@router.get("", response_model=list[MessageResponse])
async def list_messags() -> list[MessageResponse]:
    return get_messages()

@router.post("", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def create_message(payload: MessageCreate) -> MessageResponse:
    return await send_message(payload.content)