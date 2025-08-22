import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from mcp_servers import MCP_SERVERS_CONFIG

async def main(): 
    model = ChatOpenAI(model='gpt-5-mini')
    memory = MemorySaver()

    mcp_client = MultiServerMCPClient(MCP_SERVERS_CONFIG)
    tools = await mcp_client.get_tools()

    system_message = '''
    Você é um agente analista financeiro e deve utilizar 
    suas ferramentas para responder ao usuário. co
    '''

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
        async for step in agent_executor.astream(
            {'messages': [input_message]}, config, steam_mode='values'
        ):
            step['messages'][-1].pretty_print()

asyncio.run(main())