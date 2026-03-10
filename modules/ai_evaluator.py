import google.generativeai as genai
import os
import json
import re
from dotenv import load_dotenv

load_dotenv(".env", override=True)

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

MODEL = "models/gemini-1.0-pro"

def extract_json(text):
    try:
        return json.loads(text)
    except:
        pass

    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            return json.loads(match.group(0))
        except:
            pass

    return None

def evaluate_candidate(resume, jd):
    prompt = f"""
    Return ONLY JSON. No markdown. No explanation.

    {{
      "match_score": "",
      "strengths": [],
      "missing_skills": [],
      "candidate_summary": "",
      "recommendation": ""
    }}

    Resume:
    {resume}

    Job Description:
    {jd}
    """

    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)
    out = extract_json(response.text)

    if out is None:
        raise ValueError("Model did not return valid JSON:\n" + response.text)

    return out
