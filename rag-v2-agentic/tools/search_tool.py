from retrieval.embedder import embed_query
from retrieval.search import search_index


def search_tool(index, chunks, query, top_k=3):
    """
    Tool: Retrieve relevant chunks for a given query
    """

    query_embedding = embed_query(query)
    indices, distances = search_index(index, query_embedding, top_k)

    results = [chunks[i] for i in indices]
    return results
