import sys
from agents import Agent, WebSearchTool
from instruction_templates import COMMON_INSTRUCTIONS_TEMPLATE


class SalesAgentFactory:
    def __init__(self):
        self._industries = [
            "Healthcare",
            "Banking, Financial Services, and Insurance",
            "Aerospace",
            "Aeronautics",
            "Biotech",
            "Defence",
            "Pharmaceutical",
            "Telecommunications",
            "Energy",
            "Oil & Gas",
            "Manufacturing",
            "Automotive",
            "Retail & E-commerce",
            "Logistics",
            "Education",
            "Legal",
            "Hospitality",
            "Construction",
            "Agricultural Tech",
            "Cybersecurity",
            "Media & Entertainment"
        ]

        self.agent_funcs = {
            self._format_function_name(industry): self._create_agent_factory(industry)
            for industry in self._industries
        }

        self.industry_agent_map = {
            self._get_description(industry): self.agent_funcs[self._format_function_name(industry)]
            for industry in self._industries
        }

    def _format_function_name(self, industry):
        return f"get_{industry.lower().replace(',', '').replace('&', 'and').replace(' ', '_')}_sales_agent"

    def _get_description(self, industry):
        return f"AI Sales Strategist for {industry}"

    def _create_agent_factory(self, industry):
        def factory(client, region):
            tools = [WebSearchTool()]
            return Agent(
                name="Assistant",
                tools=tools,
                handoff_description=self._get_description(industry),
                instructions=COMMON_INSTRUCTIONS_TEMPLATE(industry, client, region)
            )
        return factory

    def __getattr__(self, name):
        if name in self.agent_funcs:
            return self.agent_funcs[name]
        raise AttributeError(f"No such sales agent: {name}")


# Instantiate factory and expose agent_funcs + industry map
factory = SalesAgentFactory()
agent_funcs = list(factory.agent_funcs.values())
industry_agent_map = factory.industry_agent_map
