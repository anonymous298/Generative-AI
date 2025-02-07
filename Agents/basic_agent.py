import datetime
from langchain_ollama import ChatOllama
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor, tool

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

llm = ChatOllama(model='deepseek-r1:1.5b')

query = 'what is the current time'

prompt_template = hub.pull('hwchase17/react')

tools = [get_system_time]

agent = create_react_agent(llm, tools, prompt_template)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

response = agent_executor.invoke({'input' : query})