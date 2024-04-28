import requests
import streamlit as st

def get_openai_response(input_text):
    response= requests.post("http://localhost:8000/essay/invoke",
                            json= {
                                'input':{
                                    'topic': input_text
                                }
                            })
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response= requests.post("http://localhost:8000/poem/invoke",
                            json= {
                                'input':{
                                    'topic': input_text
                                }
                            })
    return response.json()['output']


st.title('Langchain with API')
input_text1 = st.text_input("write an essay")
input_text2 = st.text_input("write a poem ")

if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))
