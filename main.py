'''
import Open-AI Agents with `pip install openai-agents`
remember to export OPENAI_API_KEY = sk..
from agents import Agent, Runner
'''
import os
import asyncio
import time
import streamlit as st
from agents import Runner
from dotenv import load_dotenv
from custom_agents import industry_agent_map


# Load environment variables from .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


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
