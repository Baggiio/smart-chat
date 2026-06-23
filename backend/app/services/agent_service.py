import logging
from functools import lru_cache

from langchain.agents import create_agent
from langchain.messages import AIMessage
from langchain_openai import ChatOpenAI

from app.core.config import get_settings
from app.tools.project_tools import get_project_context

logger = logging.getLogger("uvicorn.error")

SYSTEM_PROMPT = """
Você é o assistente virtual do Smart Chat.

Responda de forma clara, objetiva e didática.

Quando o usuário perguntar sobre a implementação, tecnologias ou arquitetura do Smar Chat,
use a ferramenta get_project_context.
Não responsa perguntas sobre o projeto usando suposições.

Para perguntas gerais, responda diretamente quando nenhuma ferramenta for necessária.
""".strip()

@lru_cache
def get_agent():
    settings = get_settings()

    model = ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key.get_secret_value(),
        timeout=30,
        max_retries=2
    )

    return create_agent(
        model=model,
        tools=[get_project_context],
        system_prompt=SYSTEM_PROMPT,
        name="smart_chat_agent"
    )

async def generate_agent_response(history: list[tuple[str, str]], content: str) -> str:
    messages = [
        {
            "role": role,
            "content": message_content
        }
        for role, message_content in history
    ]

    messages.append({
        "role": "user",
        "content": content
    })

    result = await get_agent().ainvoke({"messages": messages})

    for message in result["messages"]:

        if isinstance(message, AIMessage) and message.tool_calls:
            tool_names = [tool_call["name"] for tool_call in message.tool_calls]

            logger.info("Agent requested tools: %s", tool_names)

    final_message = result["messages"][-1]

    if not isinstance(final_message, AIMessage):
        raise RuntimeError("Agent did not return a final AI message")
    
    final_text = final_message.text.strip()

    if not final_text:
        raise RuntimeError("Agent returned an empty response")
    
    return final_text