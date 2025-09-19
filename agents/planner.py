from langchain_groq import ChatGroq
from states import *
from prompts.planner import planner_prompt


def planner_agent(state:dict)->dict:
     print("Planner Agent is starting")
     user_prompt=state["user_prompt"]
     llm=ChatGroq(model="openai/gpt-oss-120b")
     res=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
     return {"plan":res}
     
    