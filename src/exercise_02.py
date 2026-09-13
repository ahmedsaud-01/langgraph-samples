from langgraph.graph import StateGraph
from typing import TypedDict
from IPython.display import display, Image

class AgentState(TypedDict):
    name: str
    age: int
    final: str

def first_node(state: AgentState) -> AgentState:
    """This is the first node of the sequence"""

    state["final"] = f"Hi {state["name"]}"

    return state

def second_node(state: AgentState) -> AgentState:
    """This is the second node of the sequence"""

    state["final"] = state["final"] + f" You are {state["age"]} years old!"

    return state


graph = StateGraph(AgentState)
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.set_finish_point("second_node")

app = graph.compile()


display(Image(app.get_graph().draw_mermaid_png))

result = app.invoke({"name": "Johny", "age": "25"})
print(result)