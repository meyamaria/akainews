from flask import Flask, request, jsonify, send_file
from tts_generator import generate_tts

app = Flask(__name__)

@app.route('/fetch_news', methods=['GET'])
def get_news():
    company = request.args.get('company')
    articles = fetch_news_articles(company)
    return jsonify(articles)

@app.route('/analyze_sentiment', methods=['POST'])
def get_sentiment():
    data = request.json
    articles = data['articles']
    sentiments = compare_sentiments(articles)
    return jsonify(sentiments.to_dict(orient='records'))

@app.route("/get_tts", methods=["GET"])
def get_tts():
    text = request.args.get("text", "")
    if not text:
        return {"error": "No text provided"}, 400
    
    audio_file = generate_tts(text)
    return send_file(audio_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
