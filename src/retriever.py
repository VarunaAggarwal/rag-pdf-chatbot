import numpy as np


def search(query, model, index, chunks, k=3):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    query_embedding = query_embedding.reshape(1, -1)

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for i in indices[0]:

        results.append(chunks[i])

    return results