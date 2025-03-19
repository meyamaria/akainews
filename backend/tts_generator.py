from TTS.api import TTS

def generate_tts(text):
    tts = TTS("tts_models/multilingual/multi-dataset/your_model").to("cpu")
    tts.tts_to_file(text=text, file_path="output.mp3", lang="hi")
    return "output.mp3"
