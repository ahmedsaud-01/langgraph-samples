from typing import Annotated, Sequence, TypedDict
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from langchain_core.messages import BaseMessage
from langchain_core.messages import ToolMessage
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from IPython.display import display, Image

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    OPENAI_API_KEY: str

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def add(a:int, b:int):
    """This tool does the addition of two integer together and returns the sum"""
    return a + b 

@tool
def subtract(a:int, b:int):
    """This tool does the subraction of one integer from second integer"""
    return b-a

@tool
def multiply(a:int, b:int):
    """This tool does the multiplication of two integers together"""
    return a*b

tools = [add, subtract, multiply]

model = ChatOpenAI(model="gpt-4o", api_key=Settings().OPENAI_API_KEY).bind_tools(tools)

def model_call(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(
        content=
        "You are my AI assistant, please answer my query to the best of your knowledge")

    response = model.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}

def should_continue(state: AgentState) -> AgentState:
    messages = state["messages"]
    last_message = messages[-1]

    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"

graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)

toolNode = ToolNode(tools=tools)
graph.add_node("tools_node", toolNode)

graph.add_edge(START, "our_agent")
graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tools_node",
        "end": END
    }
)

graph.add_edge("tools_node", "our_agent")

agent = graph.compile()


def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()



inputs = {"messages": [("user", "add 3 and 4 and then add 7 and then multiply it")]}
print_stream(agent.stream(inputs, stream_mode="values"))