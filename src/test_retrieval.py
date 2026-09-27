from load_documents import load_pdfs
from chunk_text import chunk_text
from embeddings import create_embeddings, model
from vector_store import create_faiss_index
from retriever import search


folder = "../data/documents"

documents = load_pdfs(folder)


for document in documents:

    chunks = chunk_text(document["text"])

    embeddings = create_embeddings(chunks)

    index = create_faiss_index(embeddings)

    query = "What is the Transformer architecture?"

    results = search(
        query,
        model,
        index,
        chunks,
        k=3
    )

    print("=" * 60)
    print("QUERY:")
    print(query)
    print("=" * 60)

    for i, result in enumerate(results):

        print("\n" + "-" * 60)
        print("RESULT", i + 1)
        print("-" * 60)

        print(result)