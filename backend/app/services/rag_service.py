import chromadb
from app.services.embedding_service import get_embedding

client = chromadb.Client()
collection = client.get_or_create_collection("codebase")

def add_document(doc_id: str, content: str):
    embedding = get_embedding(content)
    collection.add(
        documents=[content],
        embeddings=[embedding],
        ids=[doc_id]
    )

def retrieve_context(query: str):
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return "\n".join(results["documents"][0])