from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")


def create_embeddings(chunks):

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    embeddings = np.asarray(embeddings)

    if embeddings.ndim == 1:

        embeddings = embeddings.reshape(1, -1)

    return embeddings