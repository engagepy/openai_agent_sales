'''
import Open-AI Agents with `pip install openai-agents`
remember to export OPENAI_API_KEY = sk..
from agents import Agent, Runner
'''
import sys
import inspect
import streamlit as st
from agents import Agent, Runner
import asyncio
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Grab the current module
current_module = sys.modules[__name__]


def COMMON_INSTRUCTIONS_TEMPLATE(industry, client, region):
    return f"""
You are an elite AI Sales Strategist for the {industry} industry, focusing exclusively on selling to {client} in the {region} market.

Your goal: Deliver a **highly personalised sales strategy** with complete awareness of client context, competitive dynamics, economic setting, regulatory mandates, and operational workflows.

Must Include:
1. **Client-Specific Research**:
   - Understand {client}'s business model, key challenges, and digital maturity.
   - Identify how AI can improve revenue, cut costs, or mitigate risk in their current workflows.

2. **Competitor Landscape**:
   - Detail how direct and adjacent competitors are leveraging AI.
   - Provide differentiators and counter-pitching ideas to win against market leaders.

3. **Regional & Industry Regulations**:
   - Lay out mandatory compliance, like {region}-specific regulations and global standards (eg. GDPR, HIPAA, FAA, etc.).
   - Include enforcement risks and how your solutions navigate them.

4. **Economic & Technological Climate**:
   - Brief on the macro-economic environment of {region} and how that impacts buyer sentiment or procurement.
   - Discuss tech adoption trends and AI readiness of the region/industry.

5. **Sales Playbook**:
   - Create 3–5 creative and actionable sales campaign ideas tailored for {client}.
   - Identify best channels, CxO language, expected objections, and ideal RoI timelines.

6. **ROI Projections**:
   - Quantify the financial or operational gain expected from each proposed AI solution.
   - Link outcomes to tangible KPIs: reduced downtime, increased sales, faster operations, better forecasting, etc.

Output must feel **custom-built** for {client} in {industry} within {region}. Avoid generic boilerplate language. Get creative but stay business-pragmatic.
"""

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

# === Agent Runner ===
async def get_agent_response(industry, client, region):
    agent_function = industry_agent_map[industry]
    agent = agent_function(client, region)
    query = f"Industry : {industry} Client : {client} Region {region}. Define the strategy and RoI."
    result = await Runner.run(agent, query)
    return result.final_output

def sync_get_agent_response(industry, client, region):
    return asyncio.run(get_agent_response(industry, client, region))

# === Streamlit UI ===
st.set_page_config(
    page_title="Enterprise AI Sales Agents",
    layout="wide",
    page_icon="",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    footer {visibility: hidden;}
    .reportview-container .main .block-container {
        padding-top: 2rem; padding-bottom: 2rem;
        background-color: #0f1117;
    }
    .stButton>button {
        background-color: #0072E3;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    h1 {
        text-align: center;
    }
    .info-card {
        background-color: #1e2130;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        border: 1px solid #333;
        color: #f0f0f0; /* Ensures text is light in both themes */
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Enterprise AI Sales Agents</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='info-card'>
    <h4>About this App</h4>
    <p>
        Each industry agent is designed by <strong>M37Labs</strong> to empower sales teams with AI-driven strategies. With each one evolving with continued research.
        It leverages specialised domain agents to create tailored pitches, competitor insights, compliance readiness,
        and region-specific intelligence — all in real-time.
    </p>
</div>
<div class='info-card'>
    <h4>How it Works</h4>
    <ul>
        <li>Search and select a specialised industry agent</li>
        <li>Provide target client and operational region</li>
        <li>Generate a detailed sales playbook with one click</li>
    </ul>
</div>
""", unsafe_allow_html=True)

industry_query = ""
industry = ""
client = ""
region = ""

display_map = {
    desc.split()[-1]: desc
    for desc in industry_agent_map.keys()
}

with st.form("sales_strategy_form"):
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1:
        selected_label = st.selectbox("Select Industry Specialisation", options=display_map.keys())
    industry = display_map[selected_label]  # Get full agent descriptor for lookup
    with col2:
        client = st.text_input("Target Enterprise Client")
    with col3:
        region = st.text_input("Region of Focus")

    submitted = st.form_submit_button("Generate Sales Strategy")

if submitted:
    if not client.strip() or not region.strip():
        st.warning("Please enter both the target enterprise client and region of focus.")
    else:
        matching_agents = [desc for desc in industry_agent_map.keys() if selected_label.lower() in desc.lower()]
        if not matching_agents:
            st.warning("No matching industry agent available. Please try a different keyword.")
        else:
            industry = matching_agents[0]
            with st.spinner("Generating AI Sales Strategy..."):
                start_time = time.time()
                try:
                    result = sync_get_agent_response(industry, client, region)
                    elapsed = round(time.time() - start_time, 2)
                    st.markdown("### Recommended Strategy")
                    st.markdown(result)
                    st.success(f"Agent Generated in {elapsed} seconds.")
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

st.markdown("""
---
<p style='text-align: center;'>Powered by <a href='https://M37Labs.com' target='_blank'>M37Labs</a></p>
""", unsafe_allow_html=True)
