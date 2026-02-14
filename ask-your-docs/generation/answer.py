from transformers import pipeline

# Load model once
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)


def generate_answer(question: str, context_chunks: list[str]) -> str:
    """
    Generate answer strictly from retrieved context
    """

    context = "\n".join(context_chunks)

    prompt = f"""
Answer the question ONLY using the context below.
If the answer is not present, say "I could not find this in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    result = qa_pipeline(prompt)
    return result[0]["generated_text"]
