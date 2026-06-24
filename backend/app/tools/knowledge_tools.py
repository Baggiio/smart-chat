import logging
from langchain.tools import tool
from app.services.retrieval_service import retrieve_project_knowledge

logger = logging.getLogger("uvicorn.error")

@tool
def search_project_knowledge(query: str) -> str:
    """
    Search the Smart Chat project documentation using semantic retrieval.

    Use this tool whenever the user asks about the Smart Chat project's
    implementation, frontend, backend, architecture, API, React Query,
    FastAPI, LangChain, PostgreSQL, pgvector, or RAG.

    Args:
        query: A complete natural-language search query describing the
            information needed from the project documentation.
    """

    logger.info(f"Executing search_project_knowledge with query {query}.")

    documents = retrieve_project_knowledge(query=query, limit=3)

    if not documents:
        return "No project documentation was found for this query."
    
    formatted_documents: list[str] = []

    for position, document in enumerate(documents, start=1):
        
        source = document.metadata.get("source", "unknown")
        start_index = document.metadata.get("start_index", "unknown")

        formatted_documents.append(
            (
                f"Result {position}\n"
                f"Source: {source}\n"
                f"Start index: {start_index}\n"
                f"Content:\n{document.page_content}"
            )
        )

    query_result = "\n\n---\n\n".join(formatted_documents)

    logger.info(f"Resultado da query: {query_result}")
    
    return query_result