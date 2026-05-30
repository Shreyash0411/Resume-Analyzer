from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from utils.document_parser import extract_text
from utils.groq_client import evaluate_candidate
import os

app = FastAPI(title="Resume Analyzer API", description="API to parse resumes and evaluate candidates using Groq LLM.")

@app.post("/api/extract-text/")
async def extract_document_text(file: UploadFile = File(...)):
    """
    Upload a resume (PDF, DOCX, TXT) and get the raw extracted text.
    This serves as the foundational parsing module for Phase 1.
    """
    try:
        content = await file.read()
        extracted_text = extract_text(file.filename, content)
        return {
            "status": "success",
            "filename": file.filename,
            "extracted_text": extracted_text
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {str(e)}")

@app.post("/api/analyze/")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(None),
    job_description_text: str = Form(None)
):
    """
    Primary analysis endpoint (Phase 3).
    Upload a resume and a job description (either as a file or plain text form data).
    Extracts text, sends to Groq API, and returns the evaluation.
    """
    try:
        # 1. Extract Resume Text
        resume_content = await resume.read()
        resume_text = extract_text(resume.filename, resume_content)
        
        # 2. Extract or Get Job Description Text
        jd_text = ""
        if job_description:
            jd_content = await job_description.read()
            jd_text = extract_text(job_description.filename, jd_content)
        elif job_description_text:
            jd_text = job_description_text
        else:
            raise HTTPException(status_code=400, detail="You must provide either a 'job_description' file or 'job_description_text'.")
            
        # 3. Send to Groq LLM for Analysis
        evaluation = evaluate_candidate(resume_text, jd_text)
        
        return {
            "status": "success",
            "resume_filename": resume.filename,
            "evaluation": evaluation
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # Handles Groq API errors or other unexpected issues
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

# Make sure the static folder exists
os.makedirs("static", exist_ok=True)

# Mount static files (like css, js)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the frontend on the root endpoint
@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")
