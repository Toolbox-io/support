import ollama

with open("context.md", "r") as f:
    context = f.read()

def answer_question_with_ollama(question, model='phi'):
    print("Thinking...")
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. Answer ONLY using the information in the text below. "
                    "If the answer is not present, say 'I don't know.'\n\n"
                    f"Text:\n{context}"
                )
            },
            {"role": "user", "content": question}
        ]
    )
    return response['message']['content'].strip()

if __name__ == "__main__":
    print("[INFO] Using Ollama LLM (phi) for generative answers.")
    while True:
        q = input("Ask a question: ")
        print("Answer:", answer_question_with_ollama(q, model='phi'))