from sentence_transformers import SentenceTransformer

# Load model once
_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts: list[str]):
    """
    Embed a list of document chunks
    """
    return _model.encode(texts, show_progress_bar=False)


def embed_query(query: str):
    """
    Embed a single user query
    """
    return _model.encode([query])[0]
