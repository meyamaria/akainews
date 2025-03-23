from gtts import gTTS
from deep_translator import GoogleTranslator

from flask import jsonify, send_from_directory
import os, io

AUDIO_DIR = "audios"


def generate_tts(text):
    translator = GoogleTranslator(source="auto", target="hi")

    translated = translator.translate(text, dest="hi")
    
    tts = gTTS(text=translated, lang="hi")
    # filename = "output.mp3"
    # filepath = os.path.join(AUDIO_DIR, filename)
    # os.makedirs(AUDIO_DIR, exist_ok=True)
    # tts.save(filepath)
    # return {"audio": f"audios/{filename}"}

    audio_io = io.BytesIO()
    tts.write_to_fp(audio_io)
    audio_io.seek(0)

    # Send headers
    # self.send_response(200)
    # self.send_header("Content-Type", "audio/mpeg")
    # self.send_header("Content-Disposition", "inline; filename=speech.mp3")
    # self.send_header("Content-Length", str(len(audio_io.getvalue())))
    # self.end_headers()
    return audio_io.read()


def returnDir(filename):
    return send_from_directory(
        AUDIO_DIR, filename, mimetype="audio/mpeg", download_name=filename
    )
