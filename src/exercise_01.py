from typing import TypedDict, List
from pydantic import BaseModel
from langgraph.graph import StateGraph
from dataclasses import dataclass

class AgentState(StateGraph):
    values: List[int]
    name: str
    result: str

def add_values(state: AgentState) -> AgentState:
    """"This function handles multiple different inputs"""

    state["result"] = f"Hi there {state["name"]}! Your sum = {list(map(lambda value: value + value, state["values"]))}"
    return state

graph = StateGraph(AgentState)
graph.add_node("add_values", add_values)

graph.set_entry_point("add_values")
graph.set_finish_point("add_values")

app = graph.compile()

from IPython.display import display, Image

display(Image(app.get_graph().draw_mermaid_png()))

answers = app.invoke({"values": [1,2,3,4], "name": "Bob"})

print(answers)