from sys import implementation

from langchain_groq import ChatGroq
from states import *
from prompts.prompt import planner_prompt, architect_prompt

from AgenticAppBuilder.prompts.prompt import coder_prompt


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

def coder_agent(state:dict)->dict:
    llm = ChatGroq(model="openai/gpt-oss-120b")
    task_plan = state["task_plan"]
    implementation_steps=task_plan["implementation_steps"]
    index=0
    step=implementation_steps[index]
    task_description=step["task_description"]
    res=llm.invoke(coder_prompt(task_description))
    code=res.content
    pass
    