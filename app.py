import streamlit as st
import requests
import json
from backend.api import get_news, get_tts, get_sentiment


st.set_page_config(page_title="News Analysis", layout="wide")

st.title("Top news of any company of your choice")

# Company Name Input
company = st.text_input("Enter Company Name", placeholder="e.g., Tesla, Google")

if st.button("Find News"):
    if company:
        with st.spinner("Fetching news..."):
            # articles = requests.get(
            #     f"http://127.0.0.1:5000/fetch_news?company={company}"
            # ).json()
            articles = get_news(company)

        if articles:
            st.write(f"## 📰 Extracted News for **{company}**")
            for article in articles:
                st.markdown(f"- [{article['title']}]({article['link']})")

            with st.spinner("Performing sentiment analysis..."):
                # sentiments = requests.post(
                #     "http://127.0.0.1:5000/sentiment_analysis",
                #     json={"articles": articles},
                # ).json()\
                sentiments = get_sentiment(articles)

            st.write("### 📈 Sentiment Analysis Results")
            st.dataframe(sentiments)

            text = " ".join([a["title"] for a in articles])
            with st.spinner("Generating Hindi audio..."):
                # audio = requests.post(
                #     "http://127.0.0.1:5000/tts_generator", json={"text": text}
                # ).json()
                # audio_url = f"http://127.0.0.1:5000/{audio['audio']}"
                audio = get_tts(text)
                # audio_url = "backend/" + audio["audio"]

            st.write("### 🔊 Listen to Titles in Hindi")
            st.audio(audio, format="audio/mp3")

        else:
            st.warning("No news articles found. Try another company.")

