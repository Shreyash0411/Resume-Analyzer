# Problem Statement: Resume Analyzer

## Background
In the modern hiring landscape, human resource departments and recruiters face an overwhelming volume of job applications for every open position. Reviewing each resume manually is a time-consuming, tedious, and error-prone process. This manual review often leads to qualified candidates being overlooked due to fatigue or human bias, while also significantly extending the time-to-hire.

## The Problem
Recruiters need a faster, more objective, and accurate way to screen and filter resumes against specific job descriptions. The lack of an automated system results in:
1. **Inefficiency:** Hundreds of hours wasted manually reading through unqualified resumes.
2. **Inconsistency & Bias:** Human review can be subjective, leading to inconsistent shortlisting.
3. **High Time-to-Hire:** Delayed screening processes increase the risk of losing top talent to competitors.
4. **Poor Candidate Experience:** Slower processes mean longer waiting times for applicants to receive feedback.

## Proposed Solution
The objective of this project is to develop an AI-powered **Resume Analyzer** utilizing the **Groq LLM API**. This system will automatically parse uploaded resumes, pass the extracted information to the Groq LLM alongside a job description, and generate a comprehensive analysis of the candidate's eligibility for the desired role.

### Key Objectives
* **Automated Parsing:** Accurately extract raw text from uploaded resume formats (PDF, DOCX, etc.).
* **LLM-Powered Analysis:** Leverage the high-speed Groq API to analyze the candidate's profile against the job requirements.
* **Eligibility Output:** Generate a clear, actionable summary of the candidate's eligibility, including matched skills, missing criteria, and an overall suitability assessment.
* **Streamlined Workflow:** Provide a simple interface where users can upload a resume and instantly receive the LLM's evaluation.

## Impact
By automating the initial screening phase with a fast and intelligent LLM (Groq), the Resume Analyzer will significantly reduce the time-to-hire, provide objective and immediate candidate evaluations, and allow HR professionals to focus their time on interviewing the most qualified individuals.
