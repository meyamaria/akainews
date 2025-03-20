import pandas as pd

def compare_sentiments(articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for article in articles:
        sentiment = analyze_sentiment(article['title'])  # Use title as a placeholder
        sentiment_counts[sentiment] += 1

    df = pd.DataFrame(sentiment_counts.items(), columns=["Sentiment", "Count"])
    return df
