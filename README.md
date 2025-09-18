# AppBuilder (Agentic AI)

An agentic app builder composed of three collaborating agents: Planner, Architect, and Coder. Built with LangChain, LangGraph, and GroqCloud LLM APIs.

## Folder Map

- `agents/`: Agent implementations and orchestration helpers
  - `planner.py`: Plans features, decomposes tasks, defines acceptance criteria
  - `architect.py`: Designs architecture, selects patterns, drafts interfaces
  - `coder.py`: Implements code, writes tests, applies fixes
- `graphs/`: LangGraph graphs and runtime definitions
- `tools/`: Reusable tools (web research, code analysis, repo actions)
- `prompts/`: Prompt templates and system instructions
- `configs/`: Configuration and model settings
- `data/`: Input/output artifacts, datasets, temp files
- `docs/`: Documentation, ADRs, diagrams
- `tests/`: Test suites and fixtures
- `scripts/`: Utility scripts (setup, maintenance)
- `logs/`: Runtime logs (git-kept)
- `workflows/`: Automation flows (local or CI orchestrations)
- `integrations/`: Third-party service clients/adapters
- `.github/`: GitHub-specific workflows and templates

## Quick Start

1. Create and populate `.env` from `.env.example`.
2. Install deps: `uv sync` (or `pip install -e .`)
3. Run: `python main.py`

## Tech

- LangChain + LangGraph for agent workflows
- GroqCloud for LLM inference
