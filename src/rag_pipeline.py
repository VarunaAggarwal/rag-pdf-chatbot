from src.load_documents import load_pdfs
from src.chunk_text import chunk_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_faiss_index
from src.retriever import search
from src.llm import generate_answer


def build_rag_pipeline(folder):

    documents = load_pdfs(folder)

    all_chunks = []

    for document in documents:

        chunks = chunk_text(document["text"])

        all_chunks.extend(chunks)

    embeddings = create_embeddings(all_chunks)

    index = create_faiss_index(embeddings)

    return index, all_chunks


def ask_question(question, index, chunks):

    results = search(
        question,
        model,
        index,
        chunks,
        k=3
    )

    context = "\n\n".join(results)

    prompt = f"""
Answer the question using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = generate_answer(prompt)

    return answer
def build_rag_from_uploaded_files(uploaded_files):

    from pypdf import PdfReader

    all_chunks = []
    all_sources = []

    for uploaded_file in uploaded_files:

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        chunks = chunk_text(text)

        all_chunks.extend(chunks)

        all_sources.extend(
            [uploaded_file.name] * len(chunks)
        )

    embeddings = create_embeddings(all_chunks)

    index = create_faiss_index(embeddings)

    return index, all_chunks, all_sources 