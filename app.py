import streamlit as st
import requests

# --- Page Configuration ---
st.set_page_config(page_title="Company News & Sentiment", layout="wide")

# --- Custom CSS for Styling ---
st.markdown(
    """
    <style>
        body {background-color: #f8f9fa; font-family: 'Arial', sans-serif;}
        .stTextInput>div>div>input {border-radius: 10px; border: 1px solid #ccc; padding: 10px;}
        .stButton>button {background-color: #4CAF50; color: white; border-radius: 5px;}
        .news-card {border-radius: 10px; background: white; padding: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
        .audio-btn {background-color: #ff5733; color: white; padding: 5px 10px; border-radius: 5px; cursor: pointer;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.title("📢 Company News & Sentiment Analysis")
st.subheader("Search for a company and get recent news with sentiment analysis.")

# --- Search Bar ---
company = st.text_input("🔍 Enter Company Name", "Tesla")
search_button = st.button("Get News")

# --- Fetch News from Backend API ---
if search_button and company:
    response = requests.get(f"http://127.0.0.1:5000/get_news?company={company}")
    if response.status_code == 200:
        news_data = response.json()
        
        # --- Display News Articles ---
        st.write("### 📰 Latest News for " + company)
        for article in news_data.get("articles", []):
            with st.container():
                st.markdown(f"""
                    <div class='news-card'>
                        <h4>{article['title']}</h4>
                        <p>{article['summary']}</p>
                        <i>Source: {article['source']} | {article['date']}</i>
                        <br>
                        <a href='{article['url']}' target='_blank'>Read More</a>
                        <br><br>
                        <button class='audio-btn' onclick="window.location.href='http://127.0.0.1:5000/get_tts?text={article['summary']}'">🔊 Listen in Hindi</button>
                    </div>
                    <br>
                """, unsafe_allow_html=True)
    else:
        st.error("❌ Unable to fetch news. Please try again later.")
