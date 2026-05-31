# 🚀 AI Resume Analyzer

An intelligent, AI-powered Resume Analyzer built with FastAPI and the Groq LLM API. This application automates the candidate screening process by evaluating a candidate's resume against a specific job description, highlighting matched skills, identifying missing requirements, and providing a final recommendation.

## 🌐 Live Demo
**Try it out here:** [https://resume-analyzer-4i7q.onrender.com/](https://resume-analyzer-4i7q.onrender.com/)

> **Note:** This application is hosted on a free Render instance. If the app hasn't been accessed for a while, the backend server will spin down to save resources. **It may take around 50 seconds to a minute to wake up** when you first visit the link. Please be patient!

## ✨ Features
*   **Automated Document Parsing:** Seamlessly extracts text from PDF, DOCX, and TXT resume files.
*   **High-Speed AI Analysis:** Utilizes the blazing-fast Groq API (`llama-3.1-8b-instant`) to perform deep cognitive analysis of the candidate's profile.
*   **Structured Feedback:** Generates a highly readable markdown report detailing overall eligibility, matched skills, missing requirements, and an actionable recommendation.
*   **Next-Gen UI:** A beautiful, responsive frontend built with modern glassmorphism design principles, dynamic glowing orbs, and smooth animations.
*   **All-in-One Deployment:** The frontend and backend are tightly integrated within FastAPI, making deployment to platforms like Render extremely simple.

## 🛠️ Tech Stack
*   **Backend:** Python, FastAPI, Uvicorn
*   **AI/LLM:** Groq API (`llama-3.1-8b-instant`)
*   **Document Parsing:** PyPDF2, python-docx
*   **Frontend:** HTML5, Vanilla CSS3 (Glassmorphism), JavaScript (marked.js)
*   **Testing:** Pytest, HTTPX

## 💻 Local Setup & Installation

Follow these steps to run the project locally on your machine.

### 1. Clone the repository
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### 2. Set up the Python Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Server
```bash
uvicorn main:app --reload
```
The application will now be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 🧪 Testing
The project includes an automated test suite. To run the tests, ensure your virtual environment is active and run:
```bash
pytest
```

## ☁️ Deployment (Render)
This application is ready to be deployed for free on [Render.com](https://render.com).
1. Create a new **Web Service** on Render and connect your GitHub repository.
2. **Build Command:** `pip install -r requirements.txt`
3. **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Environment Variables:** Add `GROQ_API_KEY` with your actual API key under the Environment tab.
