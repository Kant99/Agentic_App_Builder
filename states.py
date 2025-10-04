# Contain all the classes and states of langgraph
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class File(BaseModel):
        path: str = Field(
        description="Relative or absolute path to the file within the project."
    )
        purpose: str = Field(
        description="A short explanation of the role or purpose of this file."
    )

class Plan(BaseModel):
        project_name: str = Field(
        description="The official name of the project, used as its identifier or title."
    )
        description: str = Field(
        description="A detailed explanation of what the project does, its purpose, and context."
    )
        techstack: list[str] = Field(
        description="A list of technologies, frameworks, or tools used in building the project."
    )
        features: list[str] = Field(
        description="A list of key functionalities, capabilities, or highlights of the project."
    )
        files: list[File] = Field(
        description="A mapping of filenames to their descriptions or contents (e.g., source files)."
    )

class ImplementationSteps(BaseModel):
        filepath:str =Field(
            description="The path to the file which needs to be modified",
        )
        task_description:str=Field(
            description="A detailed description of the task to be performed on the file, Example:Add a function for addition,subtraction,multiplication and division in index.js file"
            )

class Task_Plan(BaseModel):
    implementation_steps:list[ImplementationSteps]=Field(
        description="A list of steps to be taken to implement the task"
    )
    model_config=ConfigDict(extra="allow")

class CoderState(BaseModel):
    task_plan: Task_Plan = Field(description="The plan for the task to be implemented")
    current_step_idx: int = Field(0, description="The index of the current step in the implementation steps")
    current_file_content: Optional[str] = Field(None,
                                                description="The content of the file currently being edited or created")