import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(model='gpt-3.5-turbo')

template = ''''
Traduz o texto do {idioma1} para o {idioma2}:
{texto}
'''

prompt_template = PromptTemplate.form_template(
    template=template
)

prompt = prompt_template.format(
    idioma1='Português',
    idioma2='Francês',
    texto='Olá, como vai você?'
)


response = model.invoke(prompt)