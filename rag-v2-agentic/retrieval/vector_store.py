import faiss
import numpy as np


def build_faiss_index(embeddings):
    """
    Build a FAISS vector index from embeddings.
    Safely handles lists, single vectors, and dtype issues.
    """

    # Convert to numpy array
    embeddings = np.array(embeddings)

    # Ensure 2D shape
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    # FAISS requires float32
    embeddings = embeddings.astype("float32")

    dim = embeddings.shape[1]

    # L2 distance index (simple & accurate)
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index
