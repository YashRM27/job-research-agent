# 🤖 Job Application Assistant

An AI-powered multi-agent system that generates a complete job application package using CrewAI and Groq LLM — in under 3 minutes.

## 🎯 What it does

Input a company name, job role, and your name — 4 AI agents collaborate to generate:

- 🔍 **Company Research Report** — culture, values, requirements, recent news
- 📄 **Personalized Cover Letter** — 250-350 words, tailored to the company
- 🎯 **Interview Prep** — 5 likely questions with tips on how to answer
- 📧 **Formal Cold Email** — ready to send to the hiring manager on LinkedIn

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **CrewAI** | Multi-agent orchestration framework |
| **Groq (LLaMA 3.3 70B)** | LLM for agent reasoning and writing |
| **Serper API** | Real-time web search tool |
| **LiteLLM** | LLM provider interface |
| **Streamlit** | Interactive web UI |
| **Python 3.11** | Core language |

## 🏗️ Project Structure

```
job_research_agent/
├── src/
│   ├── __init__.py
│   ├── agents.py        # 4 Agent definitions
│   └── tasks.py         # 4 Task definitions
├── app.py               # Streamlit UI
├── main.py              # Terminal entry point
├── .env                 # API keys (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 How it works

```
User Input (Company + Role + Name)
            ↓
Researcher Agent → Searches web → Research Report
            ↓
Writer Agent → Reads research → Cover Letter
            ↓
Coach Agent → Reads research → 5 Interview Questions + Tips
            ↓
Emailer Agent → Reads research → Formal Cold Email
            ↓
All 4 outputs displayed in Streamlit tabs
```

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YashRM27/job-research-agent.git
cd job-research-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file
```
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

## 🔑 Get Free API Keys

- **Groq API** (Free LLM): https://console.groq.com
- **Serper API** (Free web search): https://serper.dev

## 🔮 Future Improvements

- [ ] RAG — upload your resume PDF for more personalized output
- [ ] Support multiple output formats (PDF, DOCX)
- [ ] Email sending integration
- [ ] Job fit score based on resume vs job description
