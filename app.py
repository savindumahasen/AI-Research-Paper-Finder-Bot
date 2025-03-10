from phi.agent  import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
import google.generativeai as genai
from dotenv  import load_dotenv
load_dotenv()
import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


if not GOOGLE_API_KEY:
    raise ValueError("GOOGLEAPIKEY is missing. Please check your .env file")
else:
    genai.configure(api_key=GOOGLE_API_KEY)


#agent = Agent(
#    tools=[GoogleSearch()],
#    model=Gemini(id="gemini-2.0-flash-exp"),
#    description="You are a research agent that helps users find the latest research papers.",
#    instructions=[
#        "Given a topic by the user, respond should be 10 latest research papers about that topic.",
#        "give the research papers abstractions,with acual links.",
#        "Search in English and French",
#    ],
#    show_tool_calls=False,
#    markdown=True,
#    debug_mode=False,
#)
#agent.print_response("How cyber attecks affected on banking sector", markdown=True)






