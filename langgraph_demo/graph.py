# ../langgraph_demo/graph.py

from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.graph import CompiledGraph
from langgraph.graph.message import add_messages
from langchain_cohere import ChatCohere

from constants import Constants as c

llm = ChatCohere(
    cohere_api_key=c.COHERE_API_KEY,
    model=c.CHAT_MODEL
)

class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State) -> dict[str, list]:
    return {"messages": [llm.invoke(state["messages"])]}


def setup_graph() -> CompiledGraph:
    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    graph = graph_builder.compile()

    return graph

def run(graph: CompiledGraph) -> None:

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["q", "quit", "exit"]:
            print("Goodbye")
            break
        for event in graph.stream({"messages": ("user", user_input)}):
            for value in event.values():
                print("Command:", value["messages"][-1].content)
