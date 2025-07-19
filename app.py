import streamlit as st
from pypdf import PdfReader
import docx
from groq import Groq
import os

from dotenv import load_dotenv
load_dotenv()

# 🔑 Set your Groq API key here
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)

# ----------- Helper Functions -----------

def extract_text_from_pdf(file) -> str:
    try:
        reader = PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"

def extract_text_from_docx(file) -> str:
    try:
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        return f"Error reading DOCX: {e}"

def analyze_resume_with_groq(resume_text: str) -> str:
    prompt = f"""
You are an AI Career Coach.

Analyze the following resume and suggest:
1. 3 best-fit job roles.
2. 5 most important upskilling suggestions.
3. Recommend one free online course (with link) for each skill.

Resume:
\"\"\"{resume_text}\"\"\"

Respond in this format:
- Job Roles:
1. ...
2. ...
3. ...

- Upskilling Suggestions:
1. ...
2. ...
3. ...
...
"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful and career-focused AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

# ----------- Streamlit UI -----------

st.set_page_config(page_title="AI Career Coach", page_icon="🧠")
st.title("🧠 Career Coach")

st.markdown("Upload your resume to get personalized job suggestions and upskilling paths powered by AI.")

uploaded_file = st.file_uploader("Choose your resume", type=["pdf", "docx"])

if uploaded_file:
    with st.spinner("📄 Extracting resume and analyzing with AI..."):
        # Extract text
        if uploaded_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("❌ Unsupported file type.")
            st.stop()

        # Validate text
        if not resume_text or resume_text.startswith("Error"):
            st.error(f"❌ Failed to extract text: {resume_text}")
            st.stop()

        # Analyze via LLM
        try:
            result = analyze_resume_with_groq(resume_text)
            st.success("✅ Resume successfully analyzed!")

            st.subheader("🧾 AI Recommendations")
            st.text_area("Generated Insights", result, height=400)

        except Exception as e:
            st.error(f"❌ Error during AI analysis: {e}")
