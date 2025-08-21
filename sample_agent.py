from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import os

from tools import get_company_info, get_current_stock_price, get_history_stock_price

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
os.environ['OPENAI_API_KEY'] = SECRET_KEY


model = ChatOpenAI(
    model='gpt-5-mini',
)

memory = MemorySaver()

system_message = '''
Você é um agente analista financeiro e deve utilizar 
suas ferramentas para responder ao usuário. 
'''

tools = [
    get_company_info,
    get_current_stock_price,
    get_history_stock_price,
]

agent_executor = create_react_agent(
    model=model,
    tools=tools,
    propmt=system_message,
    checkpointer=memory,
)

config = {'configurable': {'thread_id':'1'}}

while True:
    input_message = {
        'role': 'user',
        'content': input('Digite: ')
    }
    for step in agent_executor.stream(
        {'messages': [input_message]}, config, steam_mode='values'
    ):
        step['messages'][-1].pretty_print()