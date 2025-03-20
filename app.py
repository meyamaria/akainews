import streamlit as st
import requests

st.set_page_config(page_title="News Sentiment Analysis", layout="wide")

st.title("📊 Company News Sentiment Analysis")

# Company Name Input
company = st.text_input("Enter Company Name", placeholder="e.g., Tesla, Google")

if st.button("Analyze News"):
    if company:
        with st.spinner("Fetching news..."):
            articles = requests.get(f"http://127.0.0.1:5000/fetch_news?company={company}").json()
        
        if articles:
            st.write(f"## 📰 Extracted News for **{company}**")
            for article in articles:
                st.markdown(f"- [{article['title']}]({article['link']})")
            
            with st.spinner("Performing sentiment analysis..."):
                sentiments = requests.post("http://127.0.0.1:5000/analyze_sentiment", json={"articles": articles}).json()
            
            st.write("### 📈 Sentiment Analysis Results")
            st.dataframe(sentiments)

            text = " ".join([a['title'] for a in articles])
            with st.spinner("Generating Hindi audio..."):
                audio = requests.post("http://127.0.0.1:5000/generate_tts", json={"text": text}).json()
            
            st.write("### 🔊 Listen to Summary in Hindi")
            st.audio(audio['audio'])
        else:
            st.warning("No news articles found. Try another company.")
