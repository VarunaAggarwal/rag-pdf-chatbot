from load_documents import load_pdfs
from chunk_text import chunk_text
from embeddings import create_embeddings


folder = "../data/documents"

documents = load_pdfs(folder)


for document in documents:

    chunks = chunk_text(document["text"])

    embeddings = create_embeddings(chunks)

    print("=" * 60)
    print("FILE:", document["filename"])
    print("=" * 60)

    print("Number of chunks:", len(chunks))
    print("Embedding shape:", embeddings.shape)