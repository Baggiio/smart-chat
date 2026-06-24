import argparse

from app.services.vector_store_service import get_vector_store

def main() -> None:
    parser = argparse.ArgumentParser(description="Search the Smart Chat knowledge base")

    parser.add_argument("query", help="Natural language search query")

    parser.add_argument(
        "--limit",
        type=int,
        default=3,
        help="Maximum number of results"
    )

    args = parser.parse_args()

    vector_store = get_vector_store()

    results = vector_store.similarity_search_with_score(query=args.query, k=args.limit)

    if not results:
        print("No relevant documents found.")
        return
    
    for position, (document, score) in enumerate(results, start=1):
        print(f"\nResult {position}")
        print(f"Score: {score:.4f}")
        print(f"Source: {document.metadata.get('source')}")
        print("Content:")
        print(document.page_content)

if __name__ == "__main__":
    main()