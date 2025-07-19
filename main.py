import os

from dotenv import load_dotenv
from yandex_cloud_ml_sdk import YCloudML
from yandex_cloud_ml_sdk._types.message import TextMessage

load_dotenv()

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

# --- Yandex Cloud settings ---
sdk = YCloudML(
    folder_id=os.getenv("YANDEX_CLOUD_FOLDER_ID"),
    auth=os.getenv("YANDEX_CLOUD_TOKEN")
)
model = sdk.models.completions("yandexgpt-lite", model_version="deprecated")
model = model.configure(temperature=0)

# --- Main Output Logic ---
def get_ai_output(question) -> str:
    print("Thinking...")

    result = model.run(
        [
            TextMessage(
                role="system",
                text=f"{instructions}\n\n## Контекст\n\n{full_context}"
            ),
            TextMessage(
                role="user",
                text=question
            )
        ]
    )

    response = ""

    for alternative in result:
        response += str(alternative.text)

    return response.strip()


# --- Main Loop ---
if __name__ == "__main__":
    while True:
        print(get_ai_output(input("Ask a question: ")))