import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://gateway.ai.cloudflare.com/v1/b8687b6abfce956eb0b143563cd63721/b-o-t/groq/chat/completions"

SYSTEM_PROMPT = (
    "You are my chat bot. You will receive a negative sentence from the user and you are bound to change the perspective into something positive. "
    "Make sure the output is in 2 lines."
)


def generate_response(prompt, model="llama-3.3-70b-versatile", temperature=0.7, max_tokens=150):
    if not API_KEY:
        return "❌ GROQ_API_KEY not found. Please create a .env file with your API key."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_completion_tokens": max_tokens
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        return "No valid response received."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


# ── UI ─────────────────────────────────────────────────────
st.set_page_config(page_title="Positivity Bot", page_icon="🌟")
st.title("🌟 Positivity Reframer")
st.caption("Turn any negative thought into a positive perspective — powered by LLaMA 3.3 via Groq.")

model = st.sidebar.selectbox("Model", ["llama-3.3-70b-versatile"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("Enter a negative sentence and get a positive reframe:")
user_input = st.text_input("Your thought:", placeholder="e.g. I failed my exam...")

if user_input:
    with st.spinner("Thinking positively..."):
        result = generate_response(user_input, model, temperature, max_tokens)
    st.success(result)
else:
    st.info("Type something negative above and press Enter.")
