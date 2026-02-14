from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text
from retrieval.embedder import embed_texts, embed_query
from retrieval.vector_store import build_faiss_index
from retrieval.search import search_index
from generation.answer import generate_answer

# Load document
text = load_pdf("data/uploads/sample.pdf")
chunks = chunk_text(text)

# Build index
embeddings = embed_texts(chunks)
index = build_faiss_index(embeddings)

# Ask question
question = "What is the main topic of this document?"
query_embedding = embed_query(question)

indices, _ = search_index(index, query_embedding, top_k=3)

relevant_chunks = [chunks[i] for i in indices]

# Generate answer
answer = generate_answer(question, relevant_chunks)

print("\nANSWER:\n")
print(answer)
