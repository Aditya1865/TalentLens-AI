import re

def clean_text(text: str):
    """Normalize resume text for downstream analysis."""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9+.,@ ]", "", text)
    return text