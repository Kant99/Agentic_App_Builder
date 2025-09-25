from dotenv import load_dotenv
from langgraph.constants import END
from langgraph.graph import StateGraph

from agents.planner import planner_agent, architect_agent

load_dotenv()

user_input="Build a calculator web app" 


graph=StateGraph(dict)
graph.add_node("planner",planner_agent)
graph.add_node("architect",architect_agent)
graph.add_edge(start_key="planner",end_key="architect")
graph.set_entry_point("planner")

agent=graph.compile()
result=agent.invoke({"user_prompt":user_input})
print(result)
