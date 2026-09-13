from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from IPython.display import display, Image

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file= ".env")
    OPENAI_API_KEY:str

class AgentState(BaseModel):
    messages: list[HumanMessage]

llm = ChatOpenAI(model = "gpt-4o", api_key= Settings().OPENAI_API_KEY)

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state.messages)
    print(f"\nAI: {response.content}")
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile();

display(Image(agent.get_graph().draw_mermaid_png()))


userinput = input("Enter: ")

while userinput != "exit":
    agent.invoke({"messages" : [HumanMessage(content=userinput)]})
    userinput = input("Enter: ")