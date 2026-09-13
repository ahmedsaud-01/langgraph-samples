from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from pydantic import BaseModel
from IPython.display import display, Image


class AgentState(BaseModel):
    number1: int
    operation: str
    number2: int
    finalNumber: int=None


def adder(state: AgentState) -> AgentState:
    """This node adds the 2 numbers"""

    state.finalNumber = state.number1 + state.number2
    return state

def subtractor(state: AgentState) -> AgentState:
    """This node substracts the 2 numbers"""

    state.finalNumber = state.number2 - state.number1
    return state

def decide_next_node(state: AgentState)-> AgentState:
    """This node will select the next node of the graph"""

    if state.operation == "+":
        return "addition_edge"

    elif state.operation == "-":
        return "subtraction_edge"


graph = StateGraph(AgentState)
graph.add_node("add_node", adder)
graph.add_node("substract_node", subtractor)
graph.add_node("router", lambda state:state)

graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    decide_next_node,
    {
        "addition_edge":"add_node",
        "subtraction_edge": "substract_node"
    }
)

graph.add_edge("add_node", END)
graph.add_edge("substract_node", END)

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({"number1": 1, "number2": 2, "operation": "+"})
print(result)

result = app.invoke({"number1": 1, "number2": 2, "operation": "-"})
print(result)