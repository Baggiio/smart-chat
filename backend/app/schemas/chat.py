from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field, field_validator

MessageRole = Literal["user", "assistant"]

class MessageCreate(BaseModel):
    content: str = Field(
        min_length=1,
        max_length=4000
    )

    @field_validator("content")
    @classmethod
    def normalize_content(cls, value: str) -> str:
        normalized_content = value.strip()

        if not normalized_content:
            raise ValueError("Message content cannot be empty")
        
        return normalized_content
    
class MessageResponse(BaseModel):
    id: str
    role: MessageRole
    content: str
    createdAt: datetime