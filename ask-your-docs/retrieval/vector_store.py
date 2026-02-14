import faiss
import numpy as np


def build_faiss_index(embeddings):
    """
    Build a FAISS index from embeddings.
    Handles list → numpy conversion safely.
    """

    # Convert to numpy array
    embeddings = np.array(embeddings)

    # Ensure 2D shape
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    embeddings = embeddings.astype("float32")

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index
