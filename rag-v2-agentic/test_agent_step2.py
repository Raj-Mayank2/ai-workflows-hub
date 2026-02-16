from agent.state import AgentState
from agent.planner import plan
from agent.retriever import retrieve_for_subquestions

from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text
from retrieval.embedder import embed_texts
from retrieval.vector_store import build_faiss_index


# Load document
text = load_pdf("data/uploads/sample.pdf")
chunks = chunk_text(text)

# Build vector store
embeddings = embed_texts(chunks)
index = build_faiss_index(embeddings)

# Create agent
question = "What are the limitations and how can they be mitigated?"
state = AgentState(question)

# Planning
state.sub_questions = plan(question)

# Retrieval
state = retrieve_for_subquestions(state, index, chunks)

print("\nSUB QUESTIONS:")
for sq in state.sub_questions:
    print("-", sq)

print("\nRETRIEVED CHUNKS:")
for c in state.retrieved_chunks[:2]:
    print("-" * 40)
    print(c[:300])
