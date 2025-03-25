from langchain_openai import OpenAI, ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
os.environ['OPENAI_API_KEY'] = SECRET_KEY

# model = OpenAI()
# response = model.invoke(
#     input='Quem foi Alan Turing?',
#     temperature=1,
#     max_tokens=500,
# )
# print(response)


model = ChatOpenAI(model='gpt-3.5-turbo')

messages=[
    {"role": "system", "content": "Você é um assistente virtual que fornece informações sobre figuras historicas. Dê respostas técnicas sobre."},
    {"role": "user", "content": "Quem foi Alan Turing?"},
]

response = model.invoke(messages)

print(response)
print(response.content)