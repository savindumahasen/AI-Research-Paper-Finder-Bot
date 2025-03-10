from phi.agent  import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
import google.generativeai as genai
from dotenv  import load_dotenv
load_dotenv()
import os

GROQ_API_KEY = os.getenv('GROQ_API_KEY')


#if not GOOGLE_API_KEY:
 #   raise ValueError("GOOGLEAPIKEY is missing. Please check your .env file")
#else:
 #   genai.configure(api_key=GOOGLE_API_KEY)

web_search_agent=Agent(
    tools=[DuckDuckGo()],
    model=Groq(id="Deepseek-R1-Distill-Llama-70b"),
    description="You are a web search agent that helps users find the latest research papers.",
    instructions=[
        "Given a topic by the user, respond should be 10 latest research papers about that topic.",
        "give the research papers abstractions,with acual links.",
        "Search in English and French",
    ],
    show_tool_calls=False,
    markdown=True,
    debug_mode=False,

)

google_search_agent = Agent(
    tools=[GoogleSearch()],
    model=Groq(id="Deepseek-R1-Distill-Llama-70b"),
    description="You are a research agent that helps users find the latest research papers.",
    instructions=[
        "Given a topic by the user, respond should be 10 latest research papers about that topic.",
        "give the research papers abstractions,with acual links.",
        "Search in English and French",
    ],
    show_tool_calls=False,
    markdown=True,
    debug_mode=False,
)


multi_ai_agent =Agent(
    team=[google_search_agent,web_search_agent],
    model=Groq(id="Deepseek-R1-Distill-Llama-70b"),
    description="You are a research agent that helps users find the latest research papers.",
    instructions=[
        "Given a topic by the user, respond should be 10 latest research papers about that topic.",
        "give the research papers abstractions,with acual research links names.",
        "Search in English and French",
    ],
    show_tool_calls=False,
    markdown=True,
    debug_mode=False,
)
multi_ai_agent.print_response("How cyber attecks affected on banking sector", markdown=True)






