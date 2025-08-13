# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent

from camel.toolkits import SearchToolkit

from camel.prompts import PromptTemplateGenerator
from camel.types import TaskType
from dotenv import load_dotenv
import pathlib

base_dir = pathlib.Path(__file__).parent.parent
env_path = base_dir / "owl" / ".env"
load_dotenv(dotenv_path=str(env_path))

def calculator(a: int, b: int):
    return a + b;

def get_secret_message():
    return "Hello, World!"

def main(key: str = 'generate_users', num_roles: int = 50, model=None):
    prompt_template = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.AI_SOCIETY, key
    )
    prompt = prompt_template.format(num_roles=num_roles)
    print(prompt)
    
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type="openai/gpt-4.1-mini",
        model_config_dict={"temperature": 0.0},
    )
    agent = ChatAgent("You are a helpful assistant.", model=model, tools=[get_secret_message], system_message="Answer in Russian")
    agent.reset()

    assistant_response = agent.step("Do you have a secret message for me?")
    print(assistant_response.msgs[0].content)


if __name__ == "__main__":
    main()