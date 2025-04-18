import sys
import inspect
from agents import Agent
from instruction_templates import COMMON_INSTRUCTIONS_TEMPLATE

# Grab the current module
current_module = sys.modules[__name__]

def get_healthcare_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Healthcare",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Healthcare", client, region)
    )

def get_banking_financial_services_and_insurance_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Banking, Financial Services, and Insurance",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Banking, Financial Services, and Insurance", client, region)
    )

def get_aerospace_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Aerospace",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Aerospace", client, region)
    )

def get_aeronautics_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Aeronautics",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Aeronautics", client, region)
    )

def get_biotech_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Biotech",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Biotech", client, region)
    )

def get_defence_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Defence",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Defence", client, region)
    )

def get_pharmaceutical_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Pharmaceutical",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Pharmaceutical", client, region)
    )

def get_telecommunications_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Telecommunications",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Telecommunications", client, region)
    )

def get_energy_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Energy",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Energy", client, region)
    )

def get_oil_and_gas_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Oil & Gas",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Oil & Gas", client, region)
    )

def get_manufacturing_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Manufacturing",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Manufacturing", client, region)
    )

def get_automotive_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Automotive",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Automotive", client, region)
    )

def get_retail_and_ecommerce_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Retail & E-commerce",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Retail & E-commerce", client, region)
    )

def get_logistics_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Logistics",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Logistics", client, region)
    )

def get_education_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Education",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Education", client, region)
    )

def get_legal_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Legal",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Legal", client, region)
    )

def get_hospitality_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Hospitality",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Hospitality", client, region)
    )

def get_construction_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Construction",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Construction", client, region)
    )

def get_agricultural_tech_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Agricultural Tech",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Agricultural Tech", client, region)
    )

def get_cybersecurity_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Cybersecurity",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Cybersecurity", client, region)
    )

def get_media_and_entertainment_sales_agent(client, region):
    return Agent(
        name="Assistant",
        handoff_description="AI Sales Strategist for Media & Entertainment",
        instructions=COMMON_INSTRUCTIONS_TEMPLATE("Media & Entertainment", client, region)
    )


agent_funcs = [
    obj for name, obj in inspect.getmembers(current_module, inspect.isfunction)
    if name.startswith("get_") and name.endswith("_sales_agent")
]

# === Map Descriptions to Agent Functions ===
industry_agent_map = {
    func(None, None).handoff_description: func
    for func in agent_funcs
}
