from sentence_transformers import SentenceTransformer

_model=SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts: list[str]):
    """
    Convert list of texts into embeddings
    """
    return _model.encode(texts, show_progress_bar=False)


def embed_query(query:str):
    """
    Convert user query into embedding
    """
    return _model.encode([query])[0]