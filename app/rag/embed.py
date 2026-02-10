import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = None
index = faiss.IndexFlatL2(384)
documents = []


def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def add_document(text: str):
    m = get_model()
    embedding = m.encode([text])
    index.add(np.array(embedding).astype("float32"))
    documents.append(text)


def search(query: str, k: int = 3):
    if len(documents) == 0:
        return []

    m = get_model()
    embedding = m.encode([query])

    k = min(k, len(documents))
    D, I = index.search(np.array(embedding).astype("float32"), k)

    results = []
    for i in I[0]:
        if i < len(documents):
            results.append(documents[i])

    return results
