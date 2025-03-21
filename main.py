# A basic chatbot using Ollama Model

import os
from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
import toml

# Load secrets
secrets = toml.load(".streamlit/secrets.toml")

# Ensure the key exists
if "LANGCHAIN_API_KEY" in secrets.get("general", {}):
    langchainkey = secrets["general"]["LANGCHAIN_API_KEY"]
    print("Loaded API Key:", langchainkey)  # Debugging
    os.environ["LANGCHAIN_API_KEY"] = langchainkey
else:
    raise ValueError("LANGCHAIN_API_KEY not found in secrets.toml")

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