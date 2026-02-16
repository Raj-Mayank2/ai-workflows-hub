def plan(question: str):
    """
    Decide how to approach the question.
    Returns a list of sub-questions.
    """

    question = question.lower()

    # Multi-part questions
    if "and" in question or "how" in question and "why" in question:
        return [
            f"What does the document say about {question}?",
            f"What explanations or reasons are mentioned for {question}?"
        ]

    # Comparison questions
    if "compare" in question or "difference" in question:
        return [
            "What is the first concept mentioned?",
            "What is the second concept mentioned?",
            "How are they different?"
        ]

    # Default: single retrieval
    return [question]
