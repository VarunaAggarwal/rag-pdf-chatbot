from load_documents import load_pdfs
from chunk_text import chunk_text


folder = "../data/documents"

documents = load_pdfs(folder)

for document in documents:

    print("=" * 60)
    print("FILE:", document["filename"])
    print("=" * 60)

    chunks = chunk_text(document["text"])

    print("Number of chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:3]):

        print("\n" + "-" * 60)
        print("CHUNK", i + 1)
        print("-" * 60)

        print(chunk[:500])