from langchain_groq import ChatGroq
from states import *
from prompts.prompt import planner_prompt, architect_prompt


def planner_agent(state:dict)->dict:
     print("Planner Agent is starting")
     user_prompt=state["user_prompt"]
     llm=ChatGroq(model="openai/gpt-oss-120b")
     res=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
     return {"plan":res}
     

def architect_agent(state:dict)->dict:
    plan:Plan=state["plan"]
    llm=ChatGroq(model="openai/gpt-oss-120b")
    res=llm.with_structured_output(Task_Plan).invoke(architect_prompt(plan))
    if res is None:
        raise ValueError("Architect doesnot return a valid prompt")
    res.plan=plan
    return {"task_plan":res}
    