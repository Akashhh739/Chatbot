import streamlit as st
import requests

# Your Groq API key (hardcoded)
API_KEY = "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"

# Cloudflare Gateway endpoint for Groq chat completions
API_URL = "https://gateway.ai.cloudflare.com/v1/b8687b6abfce956eb0b143563cd63721/b-o-t/groq/chat/completions"

def generate_response(prompt, model="llama-3.3-70b-versatile", temperature=0.7, max_tokens=150):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": model,
        "messages": [
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

st.title("Groq Chatbot via Cloudflare Gateway")

# Sidebar for selecting model and parameters
model = st.sidebar.selectbox("Select Model", ["llama-3.3-70b-versatile"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Completion Tokens", min_value=50, max_value=300, value=150)

st.write("Enter your prompt and get a response:")
user_input = st.text_input("Your prompt:")

if user_input:
    result = generate_response(user_input, model, temperature, max_tokens)
    st.write("🤖 Response:", result)
else:
        st.write("Waiting for your prompt...")
        st.write("🤖 Response:", result)
else:
        st.write("Waiting for your prompt...")

