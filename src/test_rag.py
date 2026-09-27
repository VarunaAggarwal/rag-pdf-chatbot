from load_documents import load_pdfs
from chunk_text import chunk_text
from embeddings import create_embeddings, model
from vector_store import create_faiss_index
from retriever import search
from llm import generate_answer


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

    context = "\n\n".join(results)

    prompt = f"""
Answer the question using only the information provided in the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    answer = generate_answer(prompt)

    print("=" * 60)
    print("QUESTION")
    print("=" * 60)

    print(query)

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(answer)