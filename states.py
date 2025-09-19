# Contain all the classes and states of langgraph
from pydantic import BaseModel, Field

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
        default_factory=dict,
        description="A mapping of filenames to their descriptions or contents (e.g., source files)."
    )