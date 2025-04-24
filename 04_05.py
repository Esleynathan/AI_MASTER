import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit



load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(model='gpt-4')

db = SQLDatabase.from_uri('sqlite:///exemplo_simples.db')

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model
)

system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=toolkit.get_tools(),
    prompt=system_message,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True,
)

prompt = '''
Use as ferramentas necessárias para responder perguntas relacionadas ao histórico de IPCA ao longo dos anos.
Responda tudo em português do brasil.
Perguntas: {q}
'''

prompt_template = PromptTemplate.from_template(prompt)

question = 'Qual mês e ano tiveram o maior IPCA?'

output = agent_executor.invoke({
    'input': prompt_template.format(q=question)
})

print(output.get('output'))