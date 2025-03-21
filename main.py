import streamlit as st
import requests
import json

# Your Groq API key (replace GROQ_TOKEN with your actual token if needed)
API_KEY = "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"

# Cloudflare Gateway endpoint for Groq chat completions (enclosed in quotes)
API_URL = "https://gateway.ai.cloudflare.com/v1/b8687b6abfce956eb0b143563cd63721/b-o-t/groq/chat/completions"

def generate_response(prompt, model="mixtral-8x7b-32768"):
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
        ]
    }
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        # For example, the response might have a structure like:
        # { "id": "...", "choices": [{ "message": { "role": "assistant", "content": "..." } }] }
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        return "No valid response received."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

st.title("Groq Chatbot via Cloudflare Gateway")

user_input = st.text_input("Your prompt:")

if user_input:
    result = generate_response(user_input)
    st.write("🤖 Response:", result)
else:
    st.write("Waiting for your prompt...")

