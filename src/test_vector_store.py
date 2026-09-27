from load_documents import load_pdfs
from chunk_text import chunk_text
from embeddings import create_embeddings
from vector_store import create_faiss_index


folder = "../data/documents"

documents = load_pdfs(folder)


for document in documents:

    chunks = chunk_text(document["text"])

    embeddings = create_embeddings(chunks)

    index = create_faiss_index(embeddings)

    print("=" * 60)
    print("FILE:", document["filename"])
    print("=" * 60)

    print("Number of chunks:", len(chunks))
    print("Embedding shape:", embeddings.shape)
    print("FAISS index size:", index.ntotal)