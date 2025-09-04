from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent

from pydantic import BaseModel, Field
from typing import List

from dotenv import load_dotenv
import pathlib

base_dir = pathlib.Path(__file__).parent.parent
env_path = base_dir / "owl" / ".env"
load_dotenv(dotenv_path=str(env_path))


class JokeResponse(BaseModel):
    joke: str = Field(description="A joke")
    funny_level: int = Field(description="Funny level, from 1 to 10")


# Create agent with structured output
model = ModelFactory.create(
    url="https://api.vsegpt.ru/v1",
    model_platform=ModelPlatformType.OPENAI,
    model_type=str(ModelPlatformType.OPENAI.value) + "/" + str(ModelType.GPT_5_MINI.value),
    model_config_dict={"temperature": 0.8, "max_tokens": 5000},
)

agent = ChatAgent(
    model=model
)

response = agent.step("Tell me a joke.", response_format=JokeResponse)

# The response content is a JSON string
print(response.msgs[0].content)
# '{"joke": "Why don't scientists trust atoms? Because they make up everything!", "funny_level": 8}'

# Access the parsed Pydantic object
parsed_response = response.msgs[0].parsed
print(parsed_response.joke)
# "Why don't scientists trust atoms? Because they make up everything!"
print(parsed_response.funny_level)
# 8