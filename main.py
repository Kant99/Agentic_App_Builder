
from langchain.globals import set_verbose, set_debug
from langgraph.constants import END
from langgraph.graph import StateGraph

from agents.planner import planner_agent, architect_agent, coder_agent



user_input="Build a calculator web app" 

set_debug(True)
set_verbose(True)

graph=StateGraph(dict)
graph.add_node("planner",planner_agent)
graph.add_node("architect",architect_agent)
graph.add_node("coder",coder_agent)

graph.add_edge("planner","architect")
graph.add_edge("architect","coder")
graph.add_conditional_edges(
    "coder",
    lambda s: "END" if s.get("status") == "DONE" else "coder",
    {"END": END, "coder": "coder"}
)
graph.set_entry_point("planner")

agent=graph.compile()

if __name__=="__main__":
    result=agent.invoke({"user_prompt":user_input})
    print(result)
