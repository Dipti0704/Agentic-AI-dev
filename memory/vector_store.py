from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Initialize embedding model
embedding = HuggingFaceEmbeddings()

# Create vector DB
db = FAISS.from_texts(["init"], embedding)

def store_memory(text: str):
    db.add_texts([text])

def search_memory(query: str):
    results = db.similarity_search(query)
    return [r.page_content for r in results]