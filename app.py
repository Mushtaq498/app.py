import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("Sentiment Analysis with Hugging Face")

user_input = st.text_input("Enter a sentence or text:")

if user_input:
    output = query({
        "inputs": user_input,
    })

    st.write("Sentiment Analysis Result:", output)
