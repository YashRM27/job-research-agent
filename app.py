import streamlit as st
from crewai import Crew, Process
from src.agents import researcher, writer, coach, emailer
from src.tasks import create_tasks

st.set_page_config(
    page_title="Job Application Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Job Application Assistant")
st.markdown("*Powered by CrewAI + Groq LLaMA 3.3 70B*")
st.divider()

company_name = st.text_input("🏢 Company Name", placeholder="e.g. Google")
job_role = st.text_input("💼 Job Role", placeholder="e.g. Data Scientist")
candidate_name = st.text_input("👤 Your Name", placeholder="e.g. Yash Mavare")

st.divider()

if st.button("🚀 Generate All", use_container_width=True):
    if not company_name or not job_role or not candidate_name:
        st.error("Please fill all fields!")
    else:
        with st.spinner("🔍 Agents working... this may take 2-3 minutes"):
            tasks = create_tasks(company_name, job_role, candidate_name)
            crew = Crew(
                agents=[researcher, writer, coach, emailer],
                tasks=tasks,
                process=Process.sequential,
                verbose=False
            )
            result = crew.kickoff()

        tab1, tab2, tab3, tab4 = st.tabs([
            "🔍 Research Report",
            "📄 Cover Letter",
            "🎯 Interview Prep",
            "📧 Cold Email"
        ])

        with tab1:
            st.markdown("### 🔍 Company Research Report")
            st.markdown(str(tasks[0].output))

        with tab2:
            st.markdown("### 📄 Cover Letter")
            st.markdown(str(tasks[1].output))
            st.download_button(
                label="⬇️ Download Cover Letter",
                data=str(tasks[1].output),
                file_name=f"cover_letter_{company_name}.txt",
                mime="text/plain"
            )

        with tab3:
            st.markdown("### 🎯 Interview Preparation")
            st.markdown(str(tasks[2].output))

        with tab4:
            st.markdown("### 📧 Cold Email")
            st.markdown(str(tasks[3].output))