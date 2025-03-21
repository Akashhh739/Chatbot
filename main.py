# A basic chatbot using Ollama Model

import os
from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
import toml
import toml

LANGCHAIN_API_KEY = "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"

# Load secrets from the file
secrets_path = ".streamlit/secrets.toml"

try:
    secrets = toml.load(secrets_path)
    print("Secrets Loaded:", secrets)  # Debugging
except FileNotFoundError:
    raise ValueError(f"secrets.toml file not found at {secrets_path}")

# Ensure the key exists in the file
if "general" in secrets and "LANGCHAIN_API_KEY" in secrets["general"]:
    langchainkey = secrets["general"]["LANGCHAIN_API_KEY"]
    print("Loaded API Key:", langchainkey)  # Debugging
else:
    raise ValueError("LANGCHAIN_API_KEY not found in secrets.toml")

# Use the key in your code
print("Using API Key:", LANGCHAIN_API_KEY)  # Debugging


load_dotenv()
langchainkey = st.secrets.get("LANGCHAIN_API_KEY", os.getenv("LANGCHAIN_API_KEY"))
os.environ["LANGCHAIN_API_KEY"] = langchainkey

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are my chat bot, you will recieve a negative sentence from user and you are bound to change the perspective into something positive ."
               "Make sure the output is in 2 lines"),
    ("user", "Question: {question}")
])

def Generate_Response(question, llm, temperature, max_tokens):
    llm = Ollama(model = llm)
    parser = StrOutputParser()
    chain = prompt|llm|parser
    answer = chain.invoke({"question": question})
    return answer

st.title("Enhanced Q&A Chatbot With Ollama")

llm = st.sidebar.selectbox("Select Open Source model",["mistral", "gemma:2b"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("Goe ahead and ask any question")
user_input=st.text_input("You:")

if user_input :
    response=Generate_Response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")
