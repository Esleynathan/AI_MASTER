import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(model='gpt-3.5-turbo')

classification_chain = (
    PromptTemplate.from_template(
        ''''
        Classifique a pergunta do usuário em um dos seguintes setores:
        - Financeiro
        - Suporte Técnico
        - Outras Informações

        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

financial_chain = (-
    PromptTemplate.from_template(
        ''''
        Você é um especialista financeiro.
        Sempre responda às perguntas começando com "Bem-vindo ao setor financeiro".
        Responsta à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
        ''''
        Você é um especialista suporte técnico.
        Sempre responda às perguntas começando com "Bem-vindo ao setor Supoerte Técnico".
        Responsta à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

other_info_chain = (
    PromptTemplate.from_template(
        ''''
        Você é um especialista informações gerais.
        Sempre responda às perguntas começando com "Bem-vindo ao setor de Central de Informações".
        Responsta à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

def route(classification):
    if 'financeiro' in classification.lower():
        return financial_chain
    elif 'técnico' in classification:
        return tech_support_chain
    else:
        return other_info_chain

pergunta = 'Como faço para alterar minha senha?'

classification = classification_chain.invoke({'pergunta': pergunta})

response_chain = route(classification=classification)

response = response_chain.invoke({'pergunta': pergunta})