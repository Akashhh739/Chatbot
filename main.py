import streamlit as st
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import requests

# Chatbot prompt definition
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are my chatbot. You will receive a negative sentence from the user and must transform it into a positive perspective."
               "Make sure the output is in 2 lines."),
    ("user", "Question: {question}")
])

def check_ollama_running():
    """Check if Ollama is running."""
    try:
        response = requests.get("http://localhost:11434/api/generate", timeout=2)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def Generate_Response(question, model, temperature, max_tokens):
    """Generate response using Ollama model."""
    if not check_ollama_running():
        return "⚠️ Error: Ollama server is not running. Start it using 'ollama serve'."

    llm = Ollama(model=model)
    parser = StrOutputParser()
    chain = prompt | llm | parser
    return chain.invoke({"question": question})

# Streamlit UI
st.title("✨ Positive Perspective Chatbot (Ollama)")

llm = st.sidebar.selectbox("Select Open Source model", ["mistral", "gemma:2b"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("🔹 Enter a negative statement, and I’ll turn it into something positive! 😊")
user_input = st.text_input("You:")

if user_input:
    response = Generate_Response(user_input, llm, temperature, max_tokens)
    st.write("🤖 Chatbot:", response)
else:
    st.write("⏳ Waiting for your input...")

