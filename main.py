from crewai import Crew, Process
from src.agents import researcher, writer
from src.tasks import create_tasks

def main():
    print("\n🤖 Welcome to Job Research Agent!\n")
    
    company_name = input("Enter company name: ")
    job_role = input("Enter job role: ")
    candidate_name = input("Enter your name: ")
    
    print(f"\n🔍 Researching {company_name} for {job_role} role...\n")
    
    tasks = create_tasks(company_name, job_role, candidate_name)
    
    crew = Crew(
        agents=[researcher, writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    
    print("\n✅ Cover Letter Generated!\n")
    print("="*50)
    print(result)
    print("="*50)
    
    # Save output to file
    with open("cover_letter.txt", "w") as f:
        f.write(str(result))
    
    print("\n📄 Cover letter saved to cover_letter.txt")

if __name__ == "__main__":
    main()