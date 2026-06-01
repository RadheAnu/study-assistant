import streamlit as st
from google import genai

import os
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

st.title("📚 AI Study Assistant")
st.caption("Ask me anything — I'll help you study!")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a study question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.history.append({"role": "user", "parts": [{"text": prompt}]})

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=st.session_state.history,
        config={
            "system_instruction": "You are a friendly study assistant. Explain topics clearly with simple language and examples. If the student asks for a quiz, generate questions on that topic."
        }
    )

    reply = response.text
    st.session_state.history.append({"role": "model", "parts": [{"text": reply}]})
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)