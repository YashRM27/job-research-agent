from crewai import Agent
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool()

researcher = Agent(
    role="Job Research Specialist",
    goal="Research the company and job role thoroughly",
    backstory="You are an expert career researcher who finds detailed information about companies and job requirements.",
    tools=[search_tool],
    llm="groq/llama-3.3-70b-versatile",
    verbose=True
)

writer = Agent(
    role="Cover Letter Writer",
    goal="Write a compelling personalized cover letter",
    backstory="You are an expert career coach who crafts tailored cover letters that get candidates noticed.",
    llm="groq/llama-3.3-70b-versatile",
    verbose=True
)
