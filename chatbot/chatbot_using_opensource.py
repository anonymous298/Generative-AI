from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import streamlit as st

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a jenius assistant, Please reply to the user."),
        ('user', 'Question: {question}')
    ]
)

st.title('Chatbot Using Open-Source Deepseek-r1-1.5b With Ollama')
user_input = st.text_input('What You Want To Search?')

# Ollama deepseek-r1:1.5b
llm = Ollama(model='deepseek-r1:1.5b')

parser = StrOutputParser()

chain = prompt | llm | parser

if st.button('Submit'):
    response = chain.invoke({'question' : user_input})
    st.write(response)