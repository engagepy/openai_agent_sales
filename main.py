import os
import asyncio
import time
import streamlit as st
from dotenv import load_dotenv
from agents import Runner, InputGuardrailTripwireTriggered
from custom_agents import industry_agent_map


# === ENVIRONMENT === #
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# === Agent Runner === #
async def get_agent_response(industry, client, region):
    agent_function = industry_agent_map[industry]
    agent = agent_function(client, region)

    query = f"Client: {client}, Industry: {industry}, Region: {region}. Generate a strategic sales plan with RoI insights."

    try:
        result = await Runner.run(agent, query, context={"industry": industry, "region": region})
        return result.final_output, None
    except InputGuardrailTripwireTriggered as e:
        output_info = getattr(e, "output_info", None)
        if output_info and hasattr(output_info, "reasoning"):
            reason = output_info.reasoning  # Use smart AI message
        elif output_info and hasattr(output_info, "reason"):
            reason = output_info.reason
        else:
            reason = "⚠️ Input rejected by AI validation agent."
        return None, reason


def sync_get_agent_response(industry, client, region):
    return asyncio.run(get_agent_response(industry, client, region))


# === Streamlit UI === #
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
    h1 { text-align: center; }
    .info-card {
        background-color: #1e2130;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        border: 1px solid #333;
        color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Enterprise AI Sales Agents</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='info-card'>
    <h4>About this App</h4>
    <p>
        Built by <strong>M37Labs</strong>, this app empowers sales teams with intelligent, real-time AI agents.
        These agents generate customised sales strategies, regional insights, and ROI-focused recommendations for any target client.
    </p>
</div>
<div class='info-card'>
    <h4>How it Works</h4>
    <ul>
        <li>Select an industry-specific AI agent</li>
        <li>Provide your target enterprise client and region</li>
        <li>Get a tailored sales playbook instantly</li>
    </ul>
</div>
""", unsafe_allow_html=True)

display_map = {
    desc.split()[-1]: desc for desc in industry_agent_map.keys()
}

with st.form("sales_strategy_form"):
    col1, col2, col3 = st.columns([3, 3, 3])
    with col1:
        selected_label = st.selectbox("Select Industry Specialisation", options=display_map.keys())
    industry = display_map[selected_label]
    with col2:
        client = st.text_input("Target Enterprise Client")
    with col3:
        region = st.text_input("Region of Focus")

    submitted = st.form_submit_button("Generate Sales Strategy")

if submitted:
    if not client.strip() or not region.strip():
        st.warning("Please enter both the target enterprise client and region of focus.")
    else:
        with st.spinner("Generating AI Sales Strategy..."):
            start_time = time.time()
            result, error = sync_get_agent_response(industry, client, region)
            elapsed = round(time.time() - start_time, 2)

            if error:
                st.error(f"🚫 Guardrail Triggered:\n\n{error}")
            else:
                st.markdown("### Recommended Strategy")
                st.markdown(result)
                st.success(f"Strategy generated in {elapsed} seconds.")

st.markdown("""
---
<p style='text-align: center;'>Powered by <a href='https://M37Labs.com' target='_blank'>M37Labs</a></p>
""", unsafe_allow_html=True)