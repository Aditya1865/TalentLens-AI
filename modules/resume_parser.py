import pdfplumber
import docx

def extract_text(file_path: str):
    """Extracts raw text from PDF, DOCX, or TXT resumes."""

    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(
                page.extract_text()
                for page in pdf.pages
                if page.extract_text()
            )

    if file_path.endswith(".docx"):
        document = docx.Document(file_path)
        return "\n".join([p.text for p in document.paragraphs])

    if file_path.endswith(".txt"):
        return open(file_path, "r").read()

    raise ValueError("Unsupported Resume Format")