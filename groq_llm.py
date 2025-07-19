from groq import Groq
import os

# Initialize the Groq client using environment variable for safety
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume_with_groq(resume_text: str) -> str:
    # Prompt to instruct the model what to do with the resume
    prompt = f"""
You are an AI Career Coach.

Analyze the following resume and suggest:
1. 3 best-fit job roles.
2. 5 most important upskilling suggestions.

Resume:
\"\"\"
{resume_text}
\"\"\"

Respond in this format:
- Job Roles:
1. ...
2. ...
3. ...

- Upskilling Suggestions:
1. ...
2. ...
3. ...
4. ...
5. ...
"""

    # Send the prompt to Groq's LLM
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful AI career assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()