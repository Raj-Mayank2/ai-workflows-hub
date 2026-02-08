from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load once at startup (kept in memory)
model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_semantic_similarity(text1: str, text2: str) -> float:
    """
    Returns similarity score between 0 and 100.
    """
    if not text1 or not text2:
        return 0.0

    emb1 = model.encode([text1])
    emb2 = model.encode([text2])

    sim = cosine_similarity(emb1, emb2)[0][0]
    return round(float(sim * 100), 2)
