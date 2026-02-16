from transformers import pipeline

qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)


def generate_answer(
    question: str,
    context_chunks: list[str],
    max_chars: int = 1200,
    max_chunks: int = 3
) -> str:
    """
    Generate a grounded answer using LIMITED context.
    """

    # Limit number of chunks
    selected_chunks = context_chunks[:max_chunks]

    # Truncate total context size
    context = ""
    for chunk in selected_chunks:
        if len(context) + len(chunk) > max_chars:
            break
        context += chunk + "\n"

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
    return result[0]["generated_text"].strip()
