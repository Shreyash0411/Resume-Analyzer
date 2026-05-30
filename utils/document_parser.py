import io
import PyPDF2
import docx

def parse_pdf(file_bytes: bytes) -> str:
    """Extract text from a PDF file."""
    reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def parse_docx(file_bytes: bytes) -> str:
    """Extract text from a DOCX file."""
    doc = docx.Document(io.BytesIO(file_bytes))
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text(filename: str, file_bytes: bytes) -> str:
    """Route to the correct parser based on file extension."""
    ext = filename.split(".")[-1].lower()
    
    if ext == "pdf":
        return parse_pdf(file_bytes)
    elif ext in ["docx", "doc"]: # Note: python-docx natively supports .docx
        return parse_docx(file_bytes)
    elif ext == "txt":
        return file_bytes.decode("utf-8", errors="ignore")
    else:
        raise ValueError(f"Unsupported file extension: .{ext}. Please upload a PDF, DOCX, or TXT file.")
