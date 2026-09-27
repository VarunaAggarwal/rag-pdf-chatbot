from src.rag_pipeline import build_rag_pipeline, ask_question


folder = "data/documents"


index, chunks = build_rag_pipeline(folder)


question = "What is the Transformer architecture?"


answer = ask_question(
    question,
    index,
    chunks
)


print("=" * 60)
print("RAG QUESTION")
print("=" * 60)

print(question)


print("\n" + "=" * 60)
print("RAG ANSWER")
print("=" * 60)

print(answer)