from llm import generate_answer


prompt = "Explain the Transformer architecture in simple terms."


answer = generate_answer(prompt)


print("=" * 60)
print("LLM RESPONSE")
print("=" * 60)

print(answer)