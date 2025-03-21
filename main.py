import streamlit as st
import requests

# Your Groq API key (hardcoded)
API_URL = "https://gateway.ai.cloudflare.com/v1/b8687b6abfce956eb0b143563cd63721/b-o-t/groq/openai/v1/chat/completions"

# Cloudflare Gateway endpoint for Chat completions
API_URL = https://gateway.ai.cloudflare.com/v1/b8687b6abfce956eb0b143563cd63721/b-o-t/groq/openai/v1/chat/completions


def generate_response(prompt, model, temperature, max_tokens):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": temperature,
        "max_completion_tokens": max_tokens
    }
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Groq Chat API typically returns a structure with "choices" array:
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        return "No valid response received."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

st.title("Chat Groq Chatbot via Cloudflare Gateway")

# Sidebar: select model and adjust parameters
model = st.sidebar.selectbox("Select Model", ["mixtral-8x7b-32768", "llama-3.3-70b-versatile"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Completion Tokens", min_value=50, max_value=300, value=150)

st.write("Enter your prompt and see the positive transformation!")
user_input = st.text_input("Your prompt:")

if user_input:
    result = generate_response(user_input, model, temperature, max_tokens)
    st.write("🤖 Response:", result)
else:
    st.write("Waiting for your prompt...")

    st.write("⏳ Waiting for your input...")


