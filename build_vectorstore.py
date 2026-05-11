import os
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create persistent Chroma database
client = chromadb.PersistentClient(path="chroma_db")

# Create or load collection
collection = client.get_or_create_collection(
    name="fitness_knowledge"
)

DATA_FOLDER = "data"

doc_id = 0

# Read all text files
for root, dirs, files in os.walk(DATA_FOLDER):

    for file in files:

        if file.endswith(".txt"):

            filepath = os.path.join(root, file)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Convert text into embedding
            embedding = model.encode(content).tolist()

            # Store in ChromaDB
            collection.add(
                documents=[content],
                embeddings=[embedding],
                ids=[str(doc_id)]
            )

            print(f"Added: {file}")

            doc_id += 1

print("Vector database created successfully!")