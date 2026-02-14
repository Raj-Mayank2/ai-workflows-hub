import faiss
import numpy as np


def build_faiss_index(embeddings: list[list[float]]):
    """
    Create FAISS index from embeddings
    """

    embeddings=np.array(embeddings).astype("float32")
    dim=embeddings.shape[1]

    index=faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index