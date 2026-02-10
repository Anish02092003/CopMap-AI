from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.IndexFlatL2(384)
documents = []


def add_document(text: str):
    embedding = model.encode([text])
    index.add(np.array(embedding).astype("float32"))
    documents.append(text)


def search(query: str, k: int = 3):
    if len(documents) == 0:
        return []

    embedding = model.encode([query])


    k = min(k, len(documents))

    D, I = index.search(np.array(embedding).astype("float32"), k)

    results = []
    for i in I[0]:
        if i < len(documents):
            results.append(documents[i])

    return results
