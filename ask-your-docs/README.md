# 📚 Ask Your Documents — RAG v1 (PDF)

A **Retrieval-Augmented Generation (RAG)** application that allows users to upload a PDF document and ask questions that are answered **strictly from the document content**.

This project demonstrates how real-world LLM systems combine **retrieval + reasoning** to produce grounded, explainable answers — without hallucination.

---

## 🎯 Project Objective

The goal of this project is to build a **from-scratch RAG pipeline** that:

- Reads and processes PDF documents
- Splits documents into meaningful chunks
- Converts chunks into embeddings
- Stores them in a vector database (FAISS)
- Retrieves relevant context for a user query
- Generates answers grounded only in retrieved data

No fine-tuning. No training. No GPU required.

---

## 🧠 Core AI Concepts Used

This project focuses on **fundamental LLM system design**, including:

- Document ingestion
- Text chunking with overlap
- Embedding generation
- Vector similarity search
- Retrieval-Augmented Generation (RAG)
- Grounded answer generation
- Explainability via retrieved context

> This is how production-grade LLM applications are built.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI)
- **Sentence Transformers (MiniLM)** — embeddings
- **FAISS (CPU)** — vector database
- **PyPDF** — PDF parsing
- **Transformers (FLAN-T5)** — answer generation

✔ CPU-only  
✔ Free & open-source  
✔ No paid APIs  

---

## 📂 Project Structure

```text
rag-v1-ask-your-docs/
│
├── app.py                  # Streamlit application
├── requirements.txt
│
├── ingestion/              # Document ingestion
│   ├── pdf_loader.py       # PDF text extraction
│   └── chunker.py          # Text chunking logic
│
├── retrieval/              # Semantic search
│   ├── embedder.py         # Embedding generation
│   ├── vector_store.py     # FAISS index creation
│   └── search.py           # Top-K retrieval
│
├── generation/             # LLM answer generation
│   └── answer.py
│
└── data/
    └── uploads/            # Uploaded PDFs
