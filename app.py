from flask import Flask, request, jsonify, send_from_directory
from google import genai

import os
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

chat_history = []
app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    user_message = request.json.get("message")
    
    chat_history.append({"role": "user", "parts": [{"text": user_message}]})
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=chat_history,
        config={
            "system_instruction": "You are a friendly study assistant. Explain topics clearly with simple language and examples. If the student asks for a quiz, generate questions on that topic."
        }
    )
    
    reply = response.text
    chat_history.append({"role": "model", "parts": [{"text": reply}]})
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)