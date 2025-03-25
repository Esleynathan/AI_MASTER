import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(model='gpt-3.5-turbo')

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content='Você deve responder baseadoem dados geográficos de reigõe do Brasl'),
        HumanMessagePromptTemplate.from_template('Por favor, me fale sobre a região {regiao}.'),
        AIMessage(content='Claro,vou começar coletando informações sobre a região {regiao} e analisando os dados disponíveis'),	
        HumanMessage(content='Certifique-se de incluir dadosdemográficos, econômicos e sociais'),
        AIMessage(content='Entendido. Aqui estão os dados:'),	
    ]
)

prompt = chat_template.format(regiao='Nordeste')

response = model.invoke(prompt)

print(response.content)