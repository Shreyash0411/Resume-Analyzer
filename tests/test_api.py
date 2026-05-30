from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """Test that the frontend is served correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Resume Analyzer" in response.text

def test_extract_text_txt():
    """Test the text extraction endpoint with a txt file."""
    file_data = b"Hello world, this is a test resume."
    response = client.post(
        "/api/extract-text/",
        files={"file": ("test.txt", file_data, "text/plain")}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "Hello world" in response.json()["extracted_text"]

def test_analyze_no_jd():
    """Test the analyze endpoint fails gracefully when JD is missing."""
    file_data = b"Candidate Name: Jane Doe."
    response = client.post(
        "/api/analyze/",
        files={"resume": ("resume.txt", file_data, "text/plain")}
    )
    # Expect 400 Bad Request because job_description or job_description_text is required
    assert response.status_code == 400
    assert "job_description" in response.json()["detail"]
