import pandas as pd
from sentiment_analysis import analyze_sentiment

def compare_sentiments(articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for article in articles:
        sentiment = analyze_sentiment(article['title'])
        sentiment_counts[sentiment] += 1

    df = pd.DataFrame(sentiment_counts.items(), columns=["Sentiment", "Count"])
    return df



