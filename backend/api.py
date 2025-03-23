from flask import Flask, request, jsonify
from tts_generator import generate_tts, returnDir
from news_scraper import fetch_news_articles
from comparative_analysis import compare_sentiments

app = Flask(__name__)

@app.route('/fetch_news', methods=['GET'])
def get_news():
    company = request.args.get('company')
    articles = fetch_news_articles(company)
    return jsonify(articles)

@app.route('/sentiment_analysis', methods=['POST'])
def get_sentiment():
    data = request.json
    articles = data['articles']
    sentiments = compare_sentiments(articles)
    return jsonify(sentiments.to_dict(orient='records'))

@app.route("/tts_generator", methods=["POST"])
def get_tts():
    data = request.json
    text = data['text']
    print(text)
    if not text:
        return {"error": "No text provided"}, 400
    
    audio_file = generate_tts(text)
    return audio_file

@app.route("/audio/<filename>")
def serve_audio(filename):
    return returnDir(filename)

if __name__ == '__main__':
    app.run(debug=True)




