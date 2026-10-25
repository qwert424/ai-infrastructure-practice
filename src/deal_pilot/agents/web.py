from collections.abc import Sequence
from typing import Any

from langchain.agents import create_agent
from langchain.tools import BaseTool
from langchain_core.runnables import Runnable
from deal_pilot.tools import web_search, fetch_url, get_current_time
from deal_pilot.utils.create_model import create_model
from deal_pilot.utils.trace_wrapper import trace_wrapper
from deal_pilot.utils.get_prompt import get_prompt
from deal_pilot.agents.agent_factory import AgentFactory


class WebAgentFactory(AgentFactory):
    @property
    def name(self) -> str:
        return "web_agent"

    async def create_agent(
        self,
        *,
        model: Any,
        system_prompt: str,
        tools: Sequence[BaseTool],
        subagents: list[dict],
        skills: list[str],
    ) -> Runnable:
        agent = create_agent(
            model=model,
            tools=tools,
            system_prompt=system_prompt,
        )
        return agent


web_agent_factory = WebAgentFactory()
factory = web_agent_factory.factory

agent_factory_with_trace = trace_wrapper(factory)
