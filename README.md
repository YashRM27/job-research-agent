# 🤖 Job Research Agent

An AI-powered multi-agent system that automatically researches companies and generates personalized cover letters using CrewAI and Groq LLM.

## 🎯 What it does

- Takes a **company name**, **job role**, and **candidate name** as input
- **Researcher Agent** searches the web for company info, culture, values, and job requirements in real time
- **Writer Agent** uses that research to generate a tailored, professional cover letter
- Saves the final cover letter to `cover_letter.txt`

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **CrewAI** | Multi-agent orchestration framework |
| **Groq (LLaMA 3.3 70B)** | LLM for agent reasoning and writing |
| **Serper API** | Real-time web search tool for agents |
| **LiteLLM** | LLM provider interface |
| **Python 3.11** | Core language |

## 🏗️ Project Structure

```
job_research_agent/
├── src/
│   ├── __init__.py
│   ├── agents.py        # Agent definitions (Researcher + Writer)
│   └── tasks.py         # Task definitions for each agent
├── main.py              # Entry point
├── .env                 # API keys (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 How it works

```
User Input (Company Name + Job Role + Candidate Name)
                    ↓
        Researcher Agent
        → Searches web in real time
        → Finds company overview, culture, values
        → Finds job role requirements
        → Finds recent company news
                    ↓
        Writer Agent
        → Reads research output
        → Crafts personalized cover letter
        → 250-350 words, professional tone
                    ↓
        Output saved to cover_letter.txt
```

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/job-research-agent.git
cd job-research-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file in root folder
```
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### 4. Run the agent
```bash
python main.py
```

### 5. Follow the prompts
```
Enter company name: Google
Enter job role: Data Scientist
Enter your name: Yash Mavare
```

## 🔑 Get Free API Keys

- **Groq API** (Free LLM): https://console.groq.com
- **Serper API** (Free web search): https://serper.dev

## 💡 Example Output

```
🤖 Welcome to Job Research Agent!

🔍 Researching Google for Data Scientist role...

[Researcher Agent working...]
→ Searching company info
→ Finding job requirements
→ Gathering recent news

[Writer Agent working...]
→ Crafting personalized cover letter

✅ Cover Letter Generated!
📄 Cover letter saved to cover_letter.txt
```

## 🔮 Future Improvements

- [ ] Add resume PDF as input for more personalized letters
- [ ] Add RAG to read candidate's own resume
- [ ] Build a Streamlit UI for non-technical users
- [ ] Support multiple output formats (PDF, DOCX)
- [ ] Add email sending functionality
