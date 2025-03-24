from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

client = OpenAI(
    api_key=SECRET_KEY,
)

audio_file = open('meu_audio.mp3', 'rb')

transcription = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file,
)

print(transcription.text)