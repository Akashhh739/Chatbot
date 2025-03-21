import streamlit as st
import requests

# Your Groq API key (hardcoded)
API_KEY = "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"

# Cloudflare Gateway endpoint (make sure this URL is correct per your account settings)
API_URL = "https://gateway.ai.cloudflare.com/v1/b8687b6abfce956eb0b143563cd63721/b-o-t/groq/chat/completions"

def generate_response(prompt, model="mixtral-8x7b-32768", temperature=0.7, max_tokens=150):
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
        # Using POST method to send the request
        response = requests.post(API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an error for non-2xx responses
        data = response.json()
        # Extract and return the response content based on the API's JSON structure
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        return "No valid response received."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

st.title("Groq Chatbot via Cloudflare Gateway")

user_input = st.text_input("Enter your prompt:")
if user_input:
    result = generate_response(user_input)
    st.write("🤖 Response:", result)
else:


