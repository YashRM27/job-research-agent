from crewai import Task
from src.agents import researcher, writer, coach, emailer

def create_tasks(company_name, job_role, candidate_name):

    research_task = Task(
        description=f"""
        Research the following in detail:
        1. What does {company_name} do? Their mission and values
        2. What are the key requirements for {job_role} role
        3. Recent news or achievements of {company_name}
        4. What kind of candidates they typically look for
        5. Company culture and work environment
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

    coach_task = Task(
        description=f"""
        Based on the research about {company_name} and the {job_role} role,
        generate exactly 5 likely interview questions the candidate will face.
        For each question provide:
        - The question itself
        - Why the interviewer is asking it
        - A tip on how to answer it effectively
        Format it clearly and professionally.
        """,
        expected_output="""5 interview questions with reasoning
        and answering tips for each.""",
        agent=coach,
        context=[research_task]
    )

    email_task = Task(
        description=f"""
        Write a formal and professional cold email that {candidate_name}
        can send to a hiring manager at {company_name}
        for the {job_role} position.
        The email should:
        - Have a formal subject line
        - Open with a professional greeting
        - Introduce {candidate_name} and their background briefly
        - Express specific interest in {company_name} and the {job_role} role
        - Highlight 2-3 key relevant skills or achievements
        - Request a brief meeting or call professionally
        - Close with a formal sign-off
        - Be between 150-200 words
        - Maintain a formal and respectful tone throughout
        """,
        expected_output="""A formal professional cold email
        with subject line, ready to send to a hiring manager.""",
        agent=emailer,
        context=[research_task]
    )

    return [research_task, write_task, coach_task, email_task]
