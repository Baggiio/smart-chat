import logging
from functools import lru_cache

from langchain.agents import create_agent
from langchain.messages import AIMessage
from langchain_openai import ChatOpenAI

from app.core.config import get_settings
from app.tools.knowledge_tools import search_project_knowledge

logger = logging.getLogger("uvicorn.error")

SYSTEM_PROMPT = """
Você é o assistente virtual do Smart Chat.

Responda de forma clara, objetiva e didática.

Sempre que o usuário perguntar sobre o projeto Smart Chat, sua
implementação, tecnologias, arquitetura, frontend, backend, API,
React Query, FastAPI, LangChain, PostgreSQL, pgvector ou RAG,
use a ferramenta search_project_knowledge antes de responder.

Baseie respostas sobre o projeto somente no contexto retornado pela
ferramenta. Não invente detalhes que não estejam na documentação.

Se o contexto recuperado não for suficiente para responder, informe
claramente que a documentação disponível não contém essa informação.

Para perguntas gerais que não sejam sobre o projeto, responda
diretamente sem utilizar a ferramenta.
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
        tools=[search_project_knowledge],
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