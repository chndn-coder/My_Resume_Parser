import fitz  # PyMuPDF
import re

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts all text from the uploaded PDF file."""
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text


def extract_basic_info(text: str) -> dict:
    """Extracts simple structured info from resume text."""
    # Find email
    email = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email = email.group(0) if email else None

    # Find phone number (simple pattern)
    phone = re.search(r'\+?\d[\d\s\-]{8,}\d', text)
    phone = phone.group(0) if phone else None

    # Guess name (take first line)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    name = lines[0] if lines else None

    # Simple keyword search for skills
    skill_keywords = ['python', 'java', 'sql', 'excel', 'react', 'html', 'css', 'javascript',
                      'machine learning', 'fastapi', 'django', 'flask', 'c++', 'data analysis']
    found_skills = [s for s in skill_keywords if s.lower() in text.lower()]

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "core_skills": ", ".join(found_skills),
    }
