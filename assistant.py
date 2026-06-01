import google.generativeai as genai

# Gemini API key
import os
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="You are a friendly study assistant. Explain topics clearly with simple language and examples. If the student asks for a quiz, generate questions on that topic."
)

chat = model.start_chat(history=[])

print("📚 Study Assistant is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye! Keep studying! 👋")
        break

    response = chat.send_message(user_input)
    print(f"\nAssistant: {response.text}\n")