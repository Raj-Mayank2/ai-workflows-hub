from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text
from retrieval.embedder import embed_texts, embed_query
from retrieval.vector_store import build_faiss_index
from retrieval.search import search_index

# Load & chunk document
text = load_pdf("data/uploads/sample.pdf")
chunks = chunk_text(text)

# Create embeddings
embeddings = embed_texts(chunks)

# Build vector store
index = build_faiss_index(embeddings)

# Query
query = "What is the main topic of this document?"
query_embedding = embed_query(query)

# Search
indices, distances = search_index(index, query_embedding)

print("\nTop matching chunks:\n")
for i in indices:
    print("-" * 40)
    print(chunks[i][:300])
