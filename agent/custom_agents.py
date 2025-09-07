from pydantic import BaseModel
from agents import (
    Agent,
    WebSearchTool,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)
from instruction_templates import COMMON_INSTRUCTIONS_TEMPLATE


# === Guardrail Output Schema === #
class IndustryRegionGuardrailOutput(BaseModel):
    is_valid: bool
    reasoning: str


# === Guardrail Agent === #
guardrail_agent = Agent(
    name="Validation Agent",
    tools=[WebSearchTool()],
    instructions=(
        "Determine if the industry and region in the user prompt are real and valid. Does the Brand belong to the industry and is active in that region ? "
        "Return is_valid = False if either is clearly wrong or fabricated. Explain why in reasoning."
    ),
    output_type=IndustryRegionGuardrailOutput
)


# === Guardrail Function === #
@input_guardrail
async def validate_client_input(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    text = input if isinstance(input, str) else str(input)

    result = await Runner.run(
        guardrail_agent,
        f"Validate this input for business industry and region relevance: {text}",
        context=ctx.context
    )

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_valid
    )


# === Main Sales Agent Factory === #
class SalesAgentFactory:
    _industries = [
        "Healthcare", "Banking", "FS", "Insurance", "Aerospace", "Aeronautics", "Biotech",
        "Defence", "Pharmaceutical", "Telecommunications", "Energy", "Oil", "Gas", "Manufacturing",
        "Automotive", "Retail", "E-commerce", "Logistics", "Education", "Legal", "Hospitality",
        "Construction", "AgriTech", "Cybersecurity", "Media", "Entertainment"
    ]

    def __init__(self):
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
                instructions=COMMON_INSTRUCTIONS_TEMPLATE(industry, client, region),
                input_guardrails=[validate_client_input]
            )
        return factory

    def __getattr__(self, name):
        if name in self.agent_funcs:
            return self.agent_funcs[name]
        raise AttributeError(f"No such sales agent: {name}")


factory = SalesAgentFactory()
agent_funcs = list(factory.agent_funcs.values())
industry_agent_map = factory.industry_agent_map 