# AI-Research-Paper-Finder-Bot
This is a multi ai agent.This research search AI agent primarily built using Phidata, Python, and the Google Gemini model.The main goal of this project is to provide users with accurate research information within minutes, minimizing time wasted on searching. Additionally, it helps users overcome difficulties in finding relevant and suitable research efficiently.


## Features

- **Web Search Agent**: 
  - Fetches research and details from web.

- **Google Search Agent**:
  - Retrieves research papers and details from google.

-  **Multi ai Agent**:
  - This agent created by combining the web_search_agent and google_search_agent both. By using this agent, users can get the web search agent and google search  agent results conclusion.

## Setup

To run the agents, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Install the required Python dependencies:

    ```terminal
    pip install -r requirements.txt
    ```

3. Create a `.env` file and include the necessary environment variables:

    ```text
    GEMINI_API_KEY = "your gemini token"
    ```

    Replace `your gemini token` with your actual API keys.


4. Run the script to start the agent:

    ```terminal
    python app.py run
    ```

## Usage
To query the agents, simply input your desired search request. The agents will process the query and give the response.

Example query:

```text
Dengue detection system for patients in SriLanka using Machine Learning
