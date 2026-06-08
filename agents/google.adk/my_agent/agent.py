from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

local_model = LiteLlm(model="ollama_chat/llama3.2:1b")

# Test tool
def get_time_from_tool(city: str) -> dict:
    """Returns fake time"""
    return """{
  "status": "success",
  "cities": [
    {
      "city": "New York",
      "timezone": "America/New_York",
      "current_time": "2026-06-08T01:09:06-04:00"
    },
    {
      "city": "London",
      "timezone": "Europe/London",
      "current_time": "2026-06-08T06:09:06+01:00"
    },
    {
      "city": "Tokyo",
      "timezone": "Asia/Tokyo",
      "current_time": "2026-06-08T14:09:06+09:00"
    },
    {
      "city": "Los Angeles",
      "timezone": "America/Los_Angeles",
      "current_time": "2026-06-07T22:09:06-07:00"
    }
  ]
}"""


root_agent = Agent(
    model=local_model,
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Provide the time to the user for requested city, if not say "I dont know"',
    tools=[get_time_from_tool]
)
