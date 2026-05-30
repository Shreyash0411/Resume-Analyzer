import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client. It will automatically look for the GROQ_API_KEY environment variable.
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def evaluate_candidate(resume_text: str, job_description: str) -> str:
    """
    Constructs the prompt and sends it to the Groq API to evaluate the candidate.
    """
    
    # Prompt Engineering Logic
    prompt = f"""
You are an expert technical recruiter and AI HR assistant. Your task is to evaluate a candidate's resume against a provided job description.

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Please provide a highly structured, analytical evaluation of the candidate. Format your response strictly in Markdown using the following structure:

### 🎯 Overall Eligibility
(Provide a concise, 2-3 sentence summary of their fit for the role)

### ✅ Matched Skills & Qualifications
* (Bullet point 1)
* (Bullet point 2)

### ❌ Missing Requirements
* (Bullet point 1)
* (Bullet point 2)

### 💡 Recommendation
(State clearly: **PROCEED TO INTERVIEW**, **REJECT**, or **KEEP ON FILE**, followed by a one-sentence justification).
"""

    try:
        # Call the Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a highly analytical HR assistant specializing in resume screening."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.1-8b-instant", # Defaulting to a fast, capable open-source model available on Groq
            temperature=0.2, # Low temperature for more deterministic, factual analysis
            max_tokens=1024
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        raise Exception(f"Failed to communicate with Groq API: {str(e)}")
