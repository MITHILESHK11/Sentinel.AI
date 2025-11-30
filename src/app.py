import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent import MonitoringAgent
from src.utils import fetch_log_content

st.set_page_config(page_title="Sentinel AI", page_icon="🛡️", layout="wide")

st.title("🛡️ Sentinel AI: Enterprise Log & Incident Agent")

# Initialize Agent
if "agent" not in st.session_state:
    try:
        st.session_state.agent = MonitoringAgent()
        st.session_state.messages = []
        st.success("Agent initialized successfully!")
    except Exception as e:
        st.error(f"Failed to initialize agent: {e}")
        st.stop()

# Sidebar for Log Analysis
with st.sidebar:
    st.header("📂 Log Analysis")
    log_source = st.text_input("Log File URL or Path", placeholder="http://example.com/error.log")
    if st.button("Analyze Log"):
        if log_source:
            with st.spinner("Fetching and analyzing log..."):
                log_content = fetch_log_content(log_source)
                if log_content.startswith("Error"):
                    st.error(log_content)
                else:
                    st.info("Log fetched. Sending to agent...")
                    response = st.session_state.agent.analyze_log(log_content)
                    st.session_state.messages.append({"role": "user", "content": f"Analyze log from: {log_source}"})
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.success("Analysis complete!")

# Chat Interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask the agent something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.send_message(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
