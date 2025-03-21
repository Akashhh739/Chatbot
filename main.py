import streamlit as st
import requests

# Define a prompt template as a string (optional)
prompt_template = (
    "You are my chatbot. You will receive a negative sentence from the user and must transform it into a positive perspective. "
    "Make sure the output is in 2 lines.\n"
    "Question: {}"
)

def Generate_Response(question, model, temperature, max_tokens):
    # Construct the prompt using the template
    prompt = prompt_template.format(question)
    
    # Define your Chat Groq API endpoint (replace with your actual endpoint)
    url = "http://localhost:8000/api/groq"  # Example URL; update as needed

    # Build the payload for Chat Groq API
    payload = {
        "prompt": prompt,
        "model": model,  # If Chat Groq supports different models, otherwise ignore
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        # Assuming the API returns a JSON object with a "response" key
        return response.json().get("response", "No response key found")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("✨ Positive Perspective Chatbot (Chat Groq)")

# Model selection (if applicable; here we only have one option)
model = st.sidebar.selectbox("Select Model", ["chat groq"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("🔹 Enter a negative statement, and I’ll turn it into something positive! 😊")
user_input = st.text_input("You:")

if user_input:
    response = Generate_Response(user_input, model, temperature, max_tokens)
    st.write("🤖 Chatbot:", response)
else:
    st.write("⏳ Waiting for your input...")


