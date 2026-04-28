from crewai import Task
from src.agents import researcher, writer

def create_tasks(company_name, job_role, candidate_name):

    research_task = Task(
        description=f"""
        Research the following:
        1. What does {company_name} do? Their mission and values
        2. What are the key requirements for {job_role} role
        3. Recent news or achievements of {company_name}
        4. What kind of candidates they typically look for
        Be specific and detailed in your findings.
        """,
        expected_output="""A detailed research report covering:
        - Company overview and culture
        - Job role requirements
        - Recent company news
        - Ideal candidate profile""",
        agent=researcher
    )

    write_task = Task(
        description=f"""
        Using the research provided, write a professional
        cover letter for {candidate_name} applying for
        {job_role} position at {company_name}.
        The letter should:
        - Be personalized to the company
        - Highlight relevant skills for the role
        - Be professional yet engaging
        - Be between 250-350 words
        """,
        expected_output="""A complete professional cover letter
        ready to send to the employer.""",
        agent=writer,
        context=[research_task]
    )

    return [research_task, write_task]
