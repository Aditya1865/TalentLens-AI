# TalentLens-AI
TalentLens AI


**AI-Powered Resume Intelligence & ATS Analytics Platform**

TalentLens AI is an intelligent candidate evaluation system that combines **ATS keyword analysis**, **LLM-based resume evaluation**, and a **visual analytics dashboard** to assist recruiters in screening and understanding candidate profiles efficiently.

The platform processes resumes, compares them against job descriptions, calculates keyword coverage, and generates an AI-based candidate assessment with structured insights.

---

## Key Features

### AI Candidate Evaluation

Uses Google's Generative AI models to evaluate resumes against job descriptions and produce structured insights such as:

* Match score (0–100)
* Candidate strengths
* Missing skills
* Summary evaluation
* Hiring recommendation

### ATS Keyword Analysis

Simulates an Applicant Tracking System by analyzing:

* Job description keywords
* Keyword density in resume
* ATS coverage percentage

### Resume Parsing

Automatically extracts text from:

* PDF resumes
* DOCX resumes
* TXT resumes

### Interactive Analytics Dashboard

The dashboard visualizes candidate evaluation data including:

* Match score distribution
* ATS coverage trends
* Candidate comparison table
* KPI metrics

### Persistent Evaluation Dataset

All evaluation results are saved to a CSV dataset, allowing:

* historical candidate analytics
* trend visualization
* model evaluation

---

## System Architecture

```
Resume Upload
      │
      ▼
Resume Parser
(PDF / DOCX / TXT)
      │
      ▼
Text Preprocessing
      │
      ▼
ATS Keyword Analyzer
      │
      ▼
AI Candidate Evaluator (LLM)
      │
      ▼
Structured JSON Output
      │
      ▼
CSV Storage
      │
      ▼
Analytics Dashboard
```

---

## Project Structure

```
TalentLens_AI
│
├── main.py
├── requirements.txt
├── README.md
│
├── modules
│   ├── ai_evaluator.py
│   ├── ats_keyword_analyzer.py
│   ├── dashboard.py
│   ├── report_generator.py
│   ├── resume_parser.py
│   └── text_preprocessor.py
│
├── output
│   └── candidate_scores.csv
│
├── uploads
│
└── .env
```

---

## Technology Stack

* Python
* Streamlit
* Pandas
* Altair
* Google Generative AI (Gemini)
* PDFPlumber
* python-docx

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/TalentLens_AI.git
cd TalentLens_AI
```

### 2. Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key
```

This key is used for the AI candidate evaluation module.

---

## Running the Application

Start the Streamlit application:

```
streamlit run main.py
```

The application will launch at:

```
http://localhost:8501
```

---

## Usage Workflow

1. Upload a resume (PDF, DOCX, or TXT)
2. Paste the job description
3. Run the evaluation
4. Review:

* AI candidate analysis
* ATS keyword coverage
* keyword density visualization

5. Explore analytics in the dashboard tab

---

## Example Output

AI Evaluation

```
{
  "match_score": 82,
  "strengths": [
    "Python",
    "Machine Learning",
    "Data Analysis"
  ],
  "missing_skills": [
    "Kubernetes",
    "Cloud Deployment"
  ],
  "candidate_summary": "...",
  "recommendation": "Recommended"
}
```

ATS Report

```
{
  "coverage_percent": 74,
  "keyword_density": [...]
}
```

---

## Future Improvements

* Resume ranking leaderboard
* AI resume improvement suggestions
* Skill radar charts
* Candidate comparison interface
* Multi-job description evaluation
* Database storage instead of CSV
* Authentication and recruiter accounts

---

## License

MIT License

---

## Author

Aditya
B.Tech – Artificial Intelligence & Machine Learning
