from tools.search_tool import search_tool


def retrieve_for_subquestions(
    state,
    index,
    chunks,
    top_k=3
):
    """
    Agent retrieves evidence per sub-question
    """

    state.retrieved_chunks = []

    for sq in state.sub_questions:
        retrieved = search_tool(index, chunks, sq, top_k)
        state.add_retrieved_chunks(retrieved)

    return state
