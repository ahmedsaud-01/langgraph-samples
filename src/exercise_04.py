from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Dict, List, Optional
from numpy import random
from pydantic import BaseModel
from IPython.display import display, Image

class AgentState(BaseModel):
    name: str
    number: list[int] = []
    counter: int

def greeting_node(state: AgentState) -> AgentState:
    """Greeting nore which says hi to the Person"""
    state.name = f"Hi there, {state.name}"
    state.counter = 0

    return state

def random_node(state: AgentState)-> AgentState:
    """Generates a random number from 0 to 10"""

    state.number.append(random.randint(0, 10))
    state.counter+=1

    return state

def should_continue(state: AgentState) -> AgentState:
    """"Node to decide what to do next"""
    if state.counter < 5:
        print("entering loop", state.counter)
        return "loop"
    else:
        return "exit"


graph = StateGraph(AgentState)
graph.add_node("greeting", greeting_node)
graph.add_node("random", random_node)
graph.add_edge("greeting", "random")

graph.add_conditional_edges(
    "random",
    should_continue,
    {
        "loop": "random",
        "exit": END
    }
)

graph.set_entry_point("greeting")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"name": "Ahmed", "counter": -100})

print(result)