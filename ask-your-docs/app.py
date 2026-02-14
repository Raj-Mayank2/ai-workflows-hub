import streamlit as st
import os

from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text

from retrieval.embedder import embed_texts, embed_query
from retrieval.vector_store import build_faiss_index
from retrieval.search import search_index

from generation.answer import generate_answer


st.set_page_config(page_title="Ask Your Docs (RAG)", layout="centered")

st.title("📚 Ask Your Documents")
st.subheader("Ask questions grounded in your PDF — no hallucinations")

st.divider()

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner("Processing document..."):
        # Save file
        os.makedirs("data/uploads", exist_ok=True)
        file_path = f"data/uploads/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Load & process
        text = load_pdf(file_path)
        chunks = chunk_text(text)

        embeddings = embed_texts(chunks)
        index = build_faiss_index(embeddings)

        # Cache in session
        st.session_state["chunks"] = chunks
        st.session_state["index"] = index

    st.success("Document processed successfully")

# ---------------- QUESTION ---------------- #

if "index" in st.session_state:

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button("Get Answer") and question.strip():

        with st.spinner("Searching document..."):
            query_embedding = embed_query(question)
            indices, distances = search_index(
                st.session_state["index"],
                query_embedding,
                top_k=3
            )

            retrieved_chunks = [
                st.session_state["chunks"][i]
                for i in indices
            ]

            answer = generate_answer(question, retrieved_chunks)

        # ---------------- OUTPUT ---------------- #

        st.markdown("### 🧠 Answer")
        st.success(answer)

        st.markdown("### 📄 Retrieved Context (Explainability)")
        for i, chunk in enumerate(retrieved_chunks):
            with st.expander(f"Chunk {i+1}"):
                st.write(chunk)
