from sklearn.metrics.pairwise import cosine_similarity
from engine.embeddings import embed

def similarity(text1:str, text2:str)->float:
    v1=embed(text1).reshape(1,-1)
    v2=embed(text2).reshape(1,-1)
    return float(cosine_similarity(v1,v2)[0][0])