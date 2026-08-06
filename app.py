from google import genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("=" * 50)
print("🤖 Welcome to Aamir's AI Assistant")
print("=" * 50)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    print("\nAI:")
    print(response.text)