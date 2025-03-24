from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

client = OpenAI(
    api_key=SECRET_KEY,
)

# ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
response = client.audio.speech.create(
    model='tss-1',
    voice='alloy',
    input='Olá, como vai?',
)

response.write_to_file('meu_audio.mp3')