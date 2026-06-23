from typing import Literal
from langchain.tools import tool

ProjectArea = Literal[
    "frontend",
    "backend",
    "ai",
    "architecture"
]

@tool
def get_project_context(area: ProjectArea) -> str:
    """
    Return information avout the Smart Chat project.
    Use this tool whenever the user asks about the project's frontend, backend, AI stack, or architecture.
    """

    project_context: dict[ProjectArea, str] = {
        "frontend": "The frontend uses React, TypeScript, Vite, Tailwind CSS and React Query.",
        "backend": "The backend uses Python and FastAPI. It exposes REST endpoints for sendind or retrieving messages.",
        "ai": "The AI layer uses LangChain with OpenAI chat model.",
        "architecture": "The frontend and backend are independent applications inside a monorepo."
    }

    return project_context[area]