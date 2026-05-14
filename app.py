import streamlit as st
from crewai import Crew, Process
from src.agents import researcher, writer
from src.tasks import create_tasks

st.set_page_config(
    page_title="Job Research Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Job Research Agent")
st.markdown("*Powered by CrewAI + Groq LLaMA 3.3 70B*")
st.divider()

company_name = st.text_input("🏢 Company Name", placeholder="e.g. Google")
job_role = st.text_input("💼 Job Role", placeholder="e.g. Data Scientist")
candidate_name = st.text_input("👤 Your Name", placeholder="e.g. Yash Mavare")

st.divider()

if st.button("🚀 Generate Cover Letter", use_container_width=True):
    if not company_name or not job_role or not candidate_name:
        st.error("Please fill all fields!")
    else:
        with st.spinner("🔍 Researcher Agent searching the web..."):
            tasks = create_tasks(company_name, job_role, candidate_name)
            crew = Crew(
                agents=[researcher, writer],
                tasks=tasks,
                process=Process.sequential,
                verbose=False
            )
            result = crew.kickoff()

        st.success("✅ Cover Letter Generated!")
        st.divider()
        st.markdown("### 📄 Your Cover Letter")
        st.markdown(str(result))

        st.download_button(
            label="⬇️ Download Cover Letter",
            data=str(result),
            file_name=f"cover_letter_{company_name}.txt",
            mime="text/plain"
        )