# Google ADK Agents

Agents in this directory are built with [Google ADK](https://google.github.io/adk-docs/).

## Setup (macOS)

### Install pip

If pip is not already installed, verify and use Python’s package manager:

```bash
pip3 --version
pip3 install google-adk
```

### Create a new agent project

```bash
adk create my_agent
```

## About `my_agent`

This starter agent shows how an agent can be hosted, invoked via prompts, and given tools to reason over context and respond.

Planned next steps:

- Add more tools so the agent can choose which one to use
- Introduce multiple agents that collaborate to complete a task
