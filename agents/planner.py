from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from states import *
from prompts.prompt import planner_prompt, architect_prompt , coder_prompt
from tools.tools import read_file, write_file, list_files, get_current_directory


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
    steps=state['task_plan'].implementation_steps
    index=0
    current_task=steps[index]
    existing_content=read_file.run(current_task.filepath)
    user_prompt = (
        f"Task: {current_task.task_description}\n"
        f"File: {current_task.filepath}\n"
        f"Existing content:\n{existing_content}\n"
        "Use write_file(path, content) to save your changes."
    )
    system_prompt=coder_prompt()
    coder_tools=[read_file, write_file, list_files, get_current_directory]
    react_agent=create_react_agent(llm,coder_tools)
    react_agent.invoke({"messages":[{"role":"system","content":system_prompt},
                                   {"role":"user","content": user_prompt}]

    })

    return {}

    