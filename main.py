import ollama

# --- Load Context and Instructions ---
try:
    with open("context/data.md", "r") as f:
        full_context = f.read()
except FileNotFoundError:
    print("Error: context/data.md not found.")
    exit()

try:
    with open("context/instruction.md", "r") as f:
        instructions = f.read()
except FileNotFoundError:
    print("Error: context/instruction.md not found.")
    exit()

def get_ai_output(question, model='phi') -> str:
    print("Thinking...")
    system_prompt = f"{instructions}\n\n## Context\n\n{full_context}"

    return ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )["message"]["content"].replace("**Answer:**", "", 1).replace("Answer:", "", 1).strip()

# --- Main Loop ---
if __name__ == "__main__":
    while True:
        print(get_ai_output(input("Ask a question: "), model='llama3:8b'))