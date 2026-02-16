from agent.state import AgentState
from agent.planner import plan
from agent.retriever import retrieve_for_subquestions
from agent.reasoner import reason_over_evidence

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

# STEP 1: Plan
state.sub_questions = plan(question)

# STEP 2: Retrieve
state = retrieve_for_subquestions(state, index, chunks)

# STEP 3: Reason
final_answer = reason_over_evidence(state)

print("\nFINAL ANSWER:\n")
print(final_answer)
