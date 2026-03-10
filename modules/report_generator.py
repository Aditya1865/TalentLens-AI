import pandas as pd
import os

def append_to_csv(ai_data: dict, ats_report: dict, output_path="output/candidate_scores.csv"):

    row = {
        "match_score": ai_data.get("match_score", ""),
        "recommendation": ai_data.get("recommendation", ""),
        "strengths": ", ".join(ai_data.get("strengths", [])),
        "missing_skills": ", ".join(ai_data.get("missing_skills", [])),
        "coverage_percent": ats_report.get("coverage_percent", 0)
    }

    df = pd.DataFrame([row])

    file_exists = os.path.isfile(output_path)
    df.to_csv(output_path, mode="a", index=False, header=not file_exists)
