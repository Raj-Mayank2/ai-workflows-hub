from generation.answer import generate_answer


def reason_over_evidence(state):
    """
    Reason over retrieved evidence and generate answers
    for each sub-question, then synthesize final answer.
    """

    final_answers = []

    for sq in state.sub_questions:
        # Use all retrieved chunks for now (simple but effective)
        answer = generate_answer(sq, state.retrieved_chunks)
        state.add_answer(answer)
        final_answers.append(answer)

    # Combine answers into a single response
    synthesized = "\n".join(
        f"- {ans}" for ans in final_answers if ans.strip()
    )

    state.mark_finished()

    return synthesized
