import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Get API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define the LLM (using OpenAI)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1, api_key=openai_api_key)

# Define the agent
email_agent = Agent(
    role="Email Generator",
    goal="Write clear, professional, and polite emails based on a given topic or phrase.",
    backstory=(
        "You are a helpful assistant who drafts well-structured emails. "
        "The emails should be polite, concise, and professional."
    ),
    llm=llm,
    verbose=True
)
