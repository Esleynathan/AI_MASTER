from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
client = OpenAI(api_key=SECRET_KEY)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um assistente virtual especializado em carro e mecânica automativa. Dê respostas técnicas sobre mecânica"},
        {"role": "user", "content": "Me fale sobre o Chevrolet Cobalt"},
    ],
)

print(response.choices[0].message.content)