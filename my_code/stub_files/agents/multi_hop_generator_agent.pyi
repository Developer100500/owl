from _typeshed import Incomplete
from camel.agents.programmed_agent_instruction import ProgrammableChatAgent, ProgrammedAgentInstructionResult, programmable_capability
from camel.datagen.source2synth.models import MultiHopQA
from typing import Any

class MultiHopGeneratorAgent(ProgrammableChatAgent):
    model_config: Incomplete
    def __init__(self, **kwargs: Any) -> None: ...
    @programmable_capability
    def generate_multi_hop_qa(self, context: str) -> ProgrammedAgentInstructionResult[MultiHopQA]: ...
