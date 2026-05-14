from crewai import Agent, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=1024
)

search_tool = SerperDevTool()

researcher = Agent(
    role="Job Research Specialist",
    goal="Research the company and job role thoroughly",
    backstory="You are an expert career researcher who finds detailed information about companies and job requirements.",
    tools=[search_tool],
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Cover Letter Writer",
    goal="Write a compelling personalized cover letter",
    backstory="You are an expert career coach who crafts tailored cover letters that get candidates noticed.",
    llm=llm,
    verbose=True
)

coach = Agent(
    role="Interview Coach",
    goal="Prepare candidates for interviews with likely questions and tips",
    backstory="You are an expert interview coach who knows exactly what interviewers look for.",
    llm=llm,
    verbose=True
)

emailer = Agent(
    role="Cold Email Specialist",
    goal="Write short compelling cold emails for job applications",
    backstory="You are an expert at writing cold emails that get responses from hiring managers.",
    llm=llm,
    verbose=True
)
