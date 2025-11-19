# DevDuck agents

A multi-agent system for Node.js programming assistance built with Google Agent Development Kit (ADK). This
project features a coordinating agent (DevDuck) that manages two specialized sub-agents (
Cerebras Agents) for different programming tasks.

## Architecture

The system consists of three main agents orchestrated by Docker Compose, which plays a
**primordial role** in launching and coordinating all agent services:

### 🐙 Docker Compose Orchestration

- **Central Role**: Docker Compose serves as the foundation for the entire multi-agent system
- **Service Orchestration**: Manages the lifecycle of all agents (DevDuck and two Cerebras sub-agents)
- **Configuration Management**: Defines agent prompts, model configurations, and service dependencies
  directly in the compose file
- **Network Coordination**: Establishes secure inter-agent communication channels
- **Environment Management**: Handles API keys, model parameters, and runtime configurations

### Agent Components

### 🦆 DevDuck (Main Agent)

- **Role**: Main development assistant and project coordinator
- **Capabilities**: Routes requests to appropriate sub-agents based on user needs

### 🧠 Cerebras Agents

- **Role**: The system features two specialized Cerebras sub-agents for different programming tasks.
- **Model**: gpt-oss-120b
- **Provider**: Cerebras API
- **Specializations**:
  - General development tasks, code explanation, and conceptual understanding.
  - Advanced computational tasks, code generation, and complex problem-solving.

## Features

- **Multi-agent coordination**: Routing between specialized agents
- **Node.js programming expertise**: All agents specialize in Node.js development
- **FastAPI web interface**: RESTful API with web interface support
- **Docker containerization**: Easy deployment with Docker Compose
- **Flexible model configuration**: Support for multiple LLM providers (local and cloud)

## Quick Start

### Prerequisites

- **[Docker Desktop] 4.43.0+ or [Docker Engine]** installed.
- If you're using Docker Engine on Linux, ensure you have [Docker Compose] 2.38.1 or later installed.

### Configuration

1. **You need a Cerebras API Key**: <https://cloud.cerebras.ai/>
2. Create a `.env` file with the following content:

```env
CEREBRAS_API_KEY=<your_cerebras_api_key>
CEREBRAS_BASE_URL=https://api.cerebras.ai/v1
CEREBRAS_CHAT_MODEL=gpt-oss-120b
```

> look at the `.env.sample` file

### ✋ All the prompts are defined in the 🐙 compose file

### Start the services

```bash
docker compose up
# if you updated the code, use --build
```

The application will be available at [http://0.0.0.0:8000](http://0.0.0.0:8000)

### Usage

The agents can be accessed through the web interface or API endpoints.

> Activate Token Streaming

**Quick Example**:

```text
Hello I'm Phil

Cerebras, generate a Node.js hello world program.

Now, add a Person class with a greet method.

Can you analyze and comment this code?

Finally, generate the tests.
```

**🎥 How to use the demo**: [https://youtu.be/WYB31bzfXnM](https://youtu.be/WYB31bzfXnM)

#### Routing Requests

- **General requests**: Handled by DevDuck, who routes to appropriate sub-agents
- **Specific agent requests**: To direct a request to a specific agent, mention its name (e.g., "Cerebras, analyze this code"). DevDuck will route the request accordingly.

## Tips

If you need to reset the conversation and return to the main coordinator, you can say:

```text
Go back to DevDuck
```

[Docker Compose]: https://github.com/docker/compose
[Docker Desktop]: https://www.docker.com/products/docker-desktop/
[Docker Engine]: https://docs.docker.com/engine/
[Docker Model Runner requirements]: https://docs.docker.com/ai/model-runner/
[Docker Offload]: https://www.docker.com/products/docker-offload/
