from langchain_groq import ChatGroq
from dotenv import load_dotenv
from states import *
from prompts.planner import planner_prompt



load_dotenv()
llm=ChatGroq(model="openai/gpt-oss-120b")
user_prompt="Create a calculator web app"
res=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
user_prompt="Build a calculator web app" 
print(res)


