# from langchain_community.tools import DuckDuckGoSearchRun

# ddg_search = DuckDuckGoSearchRun()
# search_result = ddg_search.run("Qual é a capital da França?")
# print(search_result)


# from langchain_experimental.utilities import PythonREPL

# python_repl = PythonREPL()
# result = python_repl.run("print(5 * 5)")
# print(result)


from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper   

wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(lang="pt")
)

wikipedia_result = wikipedia.run("Qual é a capital da França?")
print(wikipedia_result)