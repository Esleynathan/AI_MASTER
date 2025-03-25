import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(model='gpt-3.5-turbo')


# loader = TextLoader('base_conhecimento.txt')
# documents = loader.load()

# loader = PyPDFLoader('base_conhecimento.pdf')
# documents = loader.load()

loader = CSVLoader('base_conhecimento.csv')
documents = loader.load()

prompt_base_conhecimento = PromptTemplate(
    input_variables=['contexto','pergunta'],
    template='''Use o seguinte contexto para responder à pergunta.
    Responda apenas com base nas informações fornecidas.
    Não utilize informações externas ao contexto:
    Contexto: {contexto}
    Pergunta: {pergunta}'''
)

chain =  prompt_base_conhecimento | model | StrOutputParser()

response = chain.invoke(
    {
    'contexto': '\n'.join(doc.page_content for doc in documents), 
    'pergunta': 'Qual óleo de motor devo usar?'}
)

print(response)