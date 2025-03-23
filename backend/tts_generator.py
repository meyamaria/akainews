
from gtts import gTTS
from googletrans import Translator
from flask import jsonify, send_from_directory
import os

AUDIO_DIR = "audios"

def generate_tts(text):
    translator = Translator()

    translated = translator.translate(text, dest='hi')
    print("Translated text:", translated.text)

    tts = gTTS(text=translated.text, lang='hi')
    filename = "output.mp3"
    filepath = os.path.join( AUDIO_DIR, filename )
    os.makedirs(AUDIO_DIR, exist_ok=True)
    tts.save(filepath)
    return jsonify({"audio": f"audio/{filename}"})

def returnDir(filename):
    return send_from_directory(
        AUDIO_DIR,
        filename,
        mimetype="audio/mpeg",
        download_name=filename
    )
