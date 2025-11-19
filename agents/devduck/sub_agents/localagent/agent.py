import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

local_agent = Agent(
    model=LiteLlm(
        model=f"cerebras/{os.environ.get('CEREBRAS_CHAT_MODEL')}",
        api_base=os.environ.get("CEREBRAS_BASE_URL"),
        api_key=os.environ.get("CEREBRAS_API_KEY"),
        temperature=0.0,
    ),
    name=os.environ.get("LOCAL_AGENT_NAME"),
    description=os.environ.get("LOCAL_AGENT_DESCRIPTION"),
    instruction=os.environ.get("LOCAL_AGENT_INSTRUCTION"),
)
