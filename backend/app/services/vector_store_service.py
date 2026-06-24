from functools import lru_cache

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

from app.core.config import get_settings

@lru_cache
def get_embeddings() -> OpenAIEmbeddings:
    settings = get_settings()

    return OpenAIEmbeddings(
        model=settings.openai_embedding_model,
        api_key=settings.openai_api_key.get_secret_value()
    )

def create_vector_store(*, reset_collection: bool = False) -> PGVector:
    settings = get_settings()

    return PGVector(
        embeddings=get_embeddings(),
        collection_name=settings.rag_collection_name,
        connection=settings.postgres_url.get_secret_value(),
        use_jsonb=True,
        pre_delete_collection=reset_collection
    )

@lru_cache
def get_vector_store() -> PGVector:
    return create_vector_store()