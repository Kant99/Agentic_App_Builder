# AppBuilder (Agentic AI)

An intelligent agentic app builder that automatically generates complete web applications from natural language descriptions. The system uses three specialized AI agents working in collaboration: **Planner**, **Architect**, and **Coder**. Built with LangChain, LangGraph, and powered by GroqCloud's LLM APIs.

## 🚀 Features

- **Natural Language to Code**: Convert simple descriptions into fully functional web applications
- **Multi-Agent Architecture**: Three specialized agents handle different aspects of development
- **Automated Project Generation**: Creates complete project structures with proper file organization
- **Safe File Operations**: Secure file handling with path validation and sandboxing
- **Structured Output**: Uses Pydantic models for reliable data validation and type safety
- **Iterative Development**: Agents can refine and improve code through multiple iterations

## 🏗️ Architecture

### Agent Workflow

The system follows a sequential workflow where each agent builds upon the previous one's output:

```
User Input → Planner → Architect → Coder → Generated Project
```

### Agent Responsibilities

#### 1. **Planner Agent** (`agents/planner.py`)
- **Purpose**: Converts user prompts into comprehensive development plans
- **Output**: Structured `Plan` object containing:
  - Project name and description
  - Technology stack recommendations
  - Feature specifications
  - File structure and purposes
- **Model**: Uses GroqCloud's `openai/gpt-oss-120b` with structured output

#### 2. **Architect Agent** (`agents/planner.py`)
- **Purpose**: Breaks down the plan into specific implementation tasks
- **Output**: `Task_Plan` with ordered implementation steps
- **Features**:
  - Creates dependency-aware task ordering
  - Specifies exact implementation details
  - Defines integration points between components
  - Ensures self-contained but connected tasks

#### 3. **Coder Agent** (`agents/planner.py`)
- **Purpose**: Implements the actual code using available tools
- **Capabilities**:
  - Reads existing files to maintain compatibility
  - Writes complete file implementations
  - Uses ReAct pattern for tool usage
  - Iterates through implementation steps
  - Maintains consistent coding standards

## 📁 Project Structure

```
AgenticAppBuilder/
├── agents/                    # Agent implementations
│   ├── __init__.py
│   └── planner.py            # All three agents (planner, architect, coder)
├── prompts/                  # Prompt templates
│   ├── __init__.py
│   └── prompt.py            # System prompts for each agent
├── tools/                   # Reusable tools for agents
│   ├── __init__.py
│   └── tools.py            # File operations, directory management
├── generated_project/       # Output directory for generated apps
│   ├── index.html          # Example: Calculator web app
│   └── utils.js            # Example: Utility functions
├── states.py               # Pydantic models for data structures
├── main.py                 # Entry point and workflow orchestration
├── pyproject.toml          # Project dependencies
└── README.md              # This file
```

## 🛠️ Tools & Capabilities

### File Operations (`tools/tools.py`)
- **`write_file(path, content)`**: Safely writes content to files within project bounds
- **`read_file(path)`**: Reads file contents with error handling
- **`list_files(directory)`**: Lists all files in a directory
- **`get_current_directory()`**: Returns current working directory
- **`run_cmd(cmd, cwd, timeout)`**: Executes shell commands safely

### Security Features
- **Path Validation**: Prevents writing outside the project directory
- **Sandboxed Execution**: All operations are contained within `generated_project/`
- **Safe Command Execution**: Timeout-protected command running

## 📊 Data Models (`states.py`)

### Core Models
- **`File`**: Represents a file with path and purpose
- **`Plan`**: Complete project specification with tech stack and features
- **`ImplementationSteps`**: Individual task with file path and description
- **`Task_Plan`**: Ordered list of implementation steps
- **`CoderState`**: Tracks current implementation progress

## 🎯 Example Usage

The system can generate various types of web applications. Here's an example of a generated calculator app:

### Input
```
"Build a calculator web app"
```

### Generated Output
- **`index.html`**: Complete HTML structure with accessibility features
- **`utils.js`**: Comprehensive utility functions for arithmetic operations
- **Additional files**: CSS, JavaScript, and other assets as needed

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- GroqCloud API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AgenticAppBuilder
   ```

2. **Install dependencies**
   ```bash
   uv sync
   # or
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file with your GroqCloud API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

### Customizing the Input

Edit the `user_input` variable in `main.py`:
```python
user_input = "Build a todo list web application with local storage"
```

## 🔧 Configuration

### Model Settings
- **Default Model**: `openai/gpt-oss-120b` (GroqCloud)
- **Structured Output**: Enabled for reliable data parsing
- **Debug Mode**: Enabled by default for development

### Project Settings
- **Output Directory**: `generated_project/`
- **File Encoding**: UTF-8
- **Command Timeout**: 30 seconds

## 🛡️ Security Considerations

- All file operations are sandboxed to the `generated_project/` directory
- Path traversal attacks are prevented through validation
- Command execution has timeout protection
- No external network access during code generation

## 🔄 Workflow Details

1. **User Input Processing**: Natural language description is captured
2. **Planning Phase**: Planner agent creates comprehensive project plan
3. **Architecture Phase**: Architect agent breaks down into implementation tasks
4. **Coding Phase**: Coder agent iteratively implements each task
5. **Output Generation**: Complete project is generated in `generated_project/`

## 🧪 Dependencies

- **LangChain** (≥0.3.27): Agent framework and tool integration
- **LangGraph** (≥0.6.7): Workflow orchestration and state management
- **LangChain-Groq** (≥0.3.8): GroqCloud LLM integration
- **Pydantic** (≥2.11.9): Data validation and structured output
- **Python** (≥3.13): Runtime environment

## 📝 Development Notes

- The system uses LangGraph's StateGraph for workflow management
- All agents share the same LLM instance for consistency
- Debug and verbose modes are enabled for development
- The workflow supports conditional edges for iterative improvement
- Generated projects are fully functional and ready to deploy

## 🤝 Contributing

This is an agentic AI system that demonstrates the power of multi-agent collaboration in software development. The modular architecture makes it easy to extend with additional agents or tools.
