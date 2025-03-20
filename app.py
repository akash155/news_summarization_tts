import streamlit as st
import requests

st.title("News Summarization & Sentiment Analysis")

company = st.text_input("Enter a company name:")

if st.button("Get News Summary"):
    response = requests.get(f"http://127.0.0.1:8000/news/{company}")
    if response.status_code == 200:
        data = response.json()
        st.write(data)

if st.button("Generate Hindi TTS"):
    response = requests.get(f"http://127.0.0.1:8000/tts/{company}")
    if response.status_code == 200:
        audio_file = response.json()["audio_file"]
        st.audio(audio_file)
