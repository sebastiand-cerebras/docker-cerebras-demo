import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .sub_agents import local_agent, cerebras_agent

root_agent = Agent(
    model=LiteLlm(
        model=f"cerebras/{os.environ.get('CEREBRAS_CHAT_MODEL')}",
        api_base=os.environ.get("CEREBRAS_BASE_URL"),
        api_key=os.environ.get("CEREBRAS_API_KEY"),
        temperature=0.0,
    ),
    name=os.environ.get("DEVDUCK_AGENT_NAME"),
    description=os.environ.get("DEVDUCK_AGENT_DESCRIPTION"),
    instruction=os.environ.get("DEVDUCK_AGENT_INSTRUCTION"),
    sub_agents=[cerebras_agent, local_agent],
)
