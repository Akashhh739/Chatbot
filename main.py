import streamlit as st
import requests

# Your Chat Groq API key (hardcoded)
API_KEY = "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"

# Replace this with the actual endpoint URL for your Chat Groq API server.
# For example, if you deploy it on Oracle Cloud or another host, update the URL accordingly.
API_URL = "https://api.groq.com/v1/infer/"  # <-- Update with your actual endpoint!

def generate_response(prompt, model, temperature, max_tokens):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,         # Model name (if applicable)
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Assuming the API returns a JSON object with a "response" field:
        return data.get("response", "No response field in API result.")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Chat Groq Chatbot")

# Sidebar for parameters
model = st.sidebar.selectbox("Select Model", ["chat_groq_model"])  # Update if you have multiple model options
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("Enter a negative statement, and I'll transform it into a positive perspective!")

user_input = st.text_input("Your prompt:")

if user_input:
    result = generate_response(user_input, model, temperature, max_tokens)
    st.write("🤖 Response:", result)
else:
    st.write("Waiting for your input...")

    st.write("⏳ Waiting for your input...")


