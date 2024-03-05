# Q&A Chatbot
from langchain.llms import OpenAI
from openai import OpenAI

#from dotenv import load_dotenv

#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os


## Function to load OpenAI model and get respones
def get_openai_response(question):
    client = OpenAI()

    completion = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=question,
    max_tokens=4000,
    temperature=0.5
    )
    response = completion.choices[0].text
    
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
