from load_documents import load_pdfs


folder = "../data/documents"

documents = load_pdfs(folder)


print(f"Number of PDFs: {len(documents)}")

for document in documents:

    print("\n" + "=" * 60)

    print("FILE:", document["filename"])

    print("=" * 60)

    print(document["text"][:500])