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

load_dotenv()
langchainkey = "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"
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
