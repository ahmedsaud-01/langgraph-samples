from typing import TypedDict, List, Union
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    OPENAI_API_KEY: str

class AgentState(TypedDict):
    messages: List[Union[AIMessage, HumanMessage]]

llm = ChatOpenAI(model = "gpt-4o", api_key= Settings().OPENAI_API_KEY)

def process(state: AgentState) -> AgentState:
    """This node will solve the request you input"""
    response = llm.invoke(state["messages"])

    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")
    print(f"Current state: {state["messages"]}")

    return state

graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

app = graph.compile()

conversation_history = []

user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = app.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    user_input = input("Enter: ")