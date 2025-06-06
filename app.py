from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
from phi.tools.googlesearch import GoogleSearch
import streamlit as st

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

#GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

#if not GOOGLE_API_KEY:
#    raise ValueError ("Google API key cannot be found")
#else:
#    genai.configure(api_key=GOOGLE_API_KEY)

# Define the Web Search Agent
web_search_agent = Agent(
    tools=[DuckDuckGo()],
    model=Groq(id="Deepseek-R1-Distill-Llama-70b"),
    description="A web search agent that helps users find the latest research papers.",
    instructions=[
        "Given a topic, return 10 latest research papers.",
        "Provide abstracts with actual links.",
        "Search results should include English and French sources."
    ],
    show_tool_calls=False,
    markdown=True,
    debug_mode=False,
)

# Define the Google Search Agent
google_search_agent = Agent(
    tools=[GoogleSearch()],
    model=Groq(id="Deepseek-R1-Distill-Llama-70b"),
    description="A research agent that helps users find the latest research papers.",
    instructions=[
        "Given a topic, return 10 latest research papers.",
        "Provide abstracts with actual links.",
        "Search results should include English and French sources."
    ],
    show_tool_calls=False,
    markdown=True,
    debug_mode=False,
)

# Multi-AI Agent combining both agents
multi_ai_agent = Agent(
    team=[google_search_agent, web_search_agent],
    model=Groq(id="Deepseek-R1-Distill-Llama-70b"),
    description="A research agent that helps users find the latest research papers.",
    instructions=[
        "Given a topic, return 10 latest research papers.",
        "Provide abstracts with actual research links and names.",
        "Search results should include English and French sources."
    ],
    show_tool_calls=False,
    markdown=True,
    debug_mode=False,
)

# Streamlit UI with enhanced design
st.set_page_config(page_title="AI Research Paper Finder", page_icon="📚", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f4f4;
    }
    .stTextInput, .stButton > button {
        font-size: 18px;
    }
    .stTextInput input {
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #4CAF50;
    }
    """,
    unsafe_allow_html=True
)

st.title("📚 AI Research Paper Finder")
st.markdown("### Find the latest research papers in just a few seconds!")

# User input with enhanced design
topic = st.text_input("🔍 Enter research topic and click the the Enter:")

if topic:
    if st.button("🔎 Generate Results"):
        with st.spinner("🔍 Searching for research papers..."):
            response = multi_ai_agent.run(topic, markdown=True)
            st.markdown("## 📖 Research Papers Found:")
            st.markdown(response.content, unsafe_allow_html=True)
else:
    st.warning("Please enter your topic")
