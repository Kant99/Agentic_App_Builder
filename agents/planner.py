from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from states import *
from prompts.prompt import planner_prompt, architect_prompt , coder_prompt
from tools.tools import read_file, write_file, list_files, get_current_directory
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")

def planner_agent(state:dict)->dict:
     print("Planner Agent is starting")
     user_prompt=state["user_prompt"]
     res=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
     return {"plan":res}
     

def architect_agent(state:dict)->dict:
    plan:Plan=state["plan"]
    res=llm.with_structured_output(Task_Plan).invoke(architect_prompt(plan))
    if res is None:
        raise ValueError("Architect doesnot return a valid prompt")
    res.plan=plan
    return {"task_plan":res}

def coder_agent(state:dict)->dict:
    coder_state = state.get("coder_state")
    if coder_state is None:
        coder_state = CoderState(task_plan=state["task_plan"],current_step_idx=0 )
    steps=coder_state.task_plan.implementation_steps
    if(coder_state.current_step_idx >= len(steps)):
        return {"coder_state":coder_state, "status":"DONE"}
    current_task=steps[coder_state.current_step_idx]
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
    coder_state.current_step_idx+=1
    return {"coder_state":coder_state}

    