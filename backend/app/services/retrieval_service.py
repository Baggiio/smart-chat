from langchain_core.documents import Document

from app.services.vector_store_service import get_vector_store

def retrieve_project_knowledge(query: str, limit: int = 3) -> list[Document]:
    vector_store = get_vector_store()

    return vector_store.similarity_search(query=query, k=limit)