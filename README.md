# Agent using Together AI and LangChain

This repository contains a project that integrates Together AI and LangChain to build an intelligent agent capable of performing various tasks. Both Together AI and LangChain is already integrated in single library called langchain_together.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Together AI](#together-ai)
- [Usage](#usage)
- [Configuration](#configuration)
- [Error](#error)

## Introduction

The goal of this project is to create an intelligent agent using the capabilities of Together AI and LangChain. These technologies enable the agent to understand and process natural language, making it suitable for a variety of applications.

## Features

- **Natural Language Processing:** The agent can understand and process natural language inputs.
- **Modular Design:** The codebase is modular, making it easy to extend and customize.
- **High Performance:** Built with performance in mind, the agent can handle complex tasks efficiently.

## Installation

To install the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Pahyn/Agent-using-Together-AI-and-LangChain.git
   ```
2. Change to the project directory:
   ```bash
   cd Agent-using-Together-AI-and-LangChain
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Together AI

Together AI provide free LLM API which can be used for small scale project. As this code published, only one model is free to use.

## Usage

To use the agent, follow these steps:

1. Configure the agent by editing the configuration file (`config.yaml` or `.venv`).
2. Run the main script:
   ```bash
   python main.py
   ```

## Configuration

The configuration file (`config.yaml` or `.venv`) allows you to customize various aspects of the agent, such as API keys, model parameters, and other settings.

## Error

There is an error when running the agent. The error is as follows:

```bash
Error in StdOutCallbackHandler.on_chain_start callback: AttributeError("'NoneType' object has no attribute 'get'")
```

The error can be avoided by turning verbose parameter to False in the AgentExecutor function.

```bash
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)
```
