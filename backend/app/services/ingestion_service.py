import hashlib
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.services.vector_store_service import create_vector_store

def load_markdown_documents(knowledge_directory: Path) -> list[Document]:
    documents: list[Document] = []

    for file_path in sorted(knowledge_directory.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")

        if not content.strip():
            continue

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": file_path.name,
                    "path": str(file_path),
                    "document_type": "project_knowledge"
                }
            )
        )
        
    return documents
    
def split_documents(documents: list[Document]) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120,
        add_start_index=True
    )

    return text_splitter.split_documents(documents)

def create_chunk_id(document: Document) -> str:
    source = document.metadata.get("source", "unknown")
    start_index = document.metadata.get("start_index", 0)

    value = (
        f"{source}:"
        f"{start_index}:"
        f"{document.page_content}"
    )

    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def ingest_knowledge_base(knowledge_directory: Path) -> int:
    documents = load_markdown_documents(knowledge_directory)

    if not documents:
        raise RuntimeError(f"No Markdown documents found in {knowledge_directory}")
    
    chunks = split_documents(documents)

    chunk_ids = [create_chunk_id(chunk) for chunk in chunks]

    vector_store = create_vector_store(reset_collection=True)

    vector_store.add_documents(documents=chunks, ids=chunk_ids)

    return len(chunks)