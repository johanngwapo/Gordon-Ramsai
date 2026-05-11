import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load Chroma database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("fitness_knowledge")


def retrieve_context(query, n_results=3):

    # Convert user query into embedding
    query_embedding = model.encode(query).tolist()

    # Search database
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    # Extract matching documents
    documents = results["documents"][0]

    # Combine into one context string
    context = "\n".join(documents)

    return context