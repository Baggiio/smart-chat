from pathlib import Path

from app.services.ingestion_service import ingest_knowledge_base

BACKEND_DIRECTORY = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIRECTORY = BACKEND_DIRECTORY / "knowledge"

def main() -> None:
    chunk_count = ingest_knowledge_base(KNOWLEDGE_DIRECTORY)

    print(f"Knowledge base ingestion completed: {chunk_count} chunks stored.")

if __name__ == "__main__":
    main()