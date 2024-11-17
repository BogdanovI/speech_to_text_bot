"""Module convert wav audio file to text with using whisper library"""

import os
import whisper
from transcoding.ogg_to_wav import transcoding_ogg_to_wav

LANGUAGE_MODEL = whisper.load_model("large")

def convert_to_text(file):
    """Convert audio file to text function"""
    file_path = transcoding_ogg_to_wav(file)
    if file_path == "error":
        os.remove(file_path)
    result = LANGUAGE_MODEL.transcribe(file_path)
    os.remove(file_path)
    text_result = result["text"]
    return text_result
