import numpy as np


def search_index(index, query_embedding, top_k: int = 3):
    """
    Search FAISS index using a query embedding.
    """

    # Ensure correct shape and dtype
    query_embedding = np.array(query_embedding).astype("float32")

    if query_embedding.ndim == 1:
        query_embedding = query_embedding.reshape(1, -1)

    distances, indices = index.search(query_embedding, top_k)

    return indices[0], distances[0]
