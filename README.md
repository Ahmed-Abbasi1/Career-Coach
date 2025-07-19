# 🧠 AI Career Coach

AI Career Coach is a **resume analyzer** powered by **Groq’s free LLMs** that provides:

- ✅ Best-fit job roles  
- 📚 Personalized upskilling recommendations  
- 🎯 Actionable feedback to boost your career

> ⚡ Fully serverless – built using **Streamlit** with **no backend required**

---

## 🔍 Features

- Upload your resume (PDF or DOCX)
- Extracts and analyzes resume content via LLM
- Returns:
  - Top 3 job roles suited to your skills
  - 5 upskilling suggestions
  - (Coming soon) Course recommendations to improve gaps

---

## 🚀 Demo

🔗 **Live App**: [Your Streamlit Link Here]  
📄 **Try with Sample**: `sample_resume.pdf`

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)  
- **AI Engine**: [Groq LLMs](https://console.groq.com)  
- **Parsing**: `pypdf`, `python-docx`  
- **Secrets Handling**: `python-dotenv` or `st.secrets`

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-career-coach.git
cd ai-career-coach

# Create and activate virtual environment
python -m venv coach
coach\Scripts\activate  # or source coach/bin/activate

# Install dependencies
pip install -r requirements.txt

GROQ_API_KEY=your_groq_api_key_here

streamlit run app.py
