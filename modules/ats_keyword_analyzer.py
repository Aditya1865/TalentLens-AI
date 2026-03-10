import re
from collections import Counter

def tokenize(text):
    return re.findall(r"[a-zA-Z0-9+.]+", text.lower())

def extract_jd_keywords(jd_text):
    tokens = tokenize(jd_text)
    tech_terms = [
        "python","sql","java","docker","aws","azure","nlp","ml","ai",
        "flask","react","node","kubernetes","api","git",
        "tensorflow","pytorch"
    ]
    return list(set([t for t in tokens if t in tech_terms]))

def compute_keyword_density(resume, jd_keywords):
    tokens = tokenize(resume)
    total = len(tokens)
    counter = Counter(tokens)

    density_list = []
    for kw in jd_keywords:
        count = counter[kw]
        density = round((count / total) * 100, 2) if total else 0
        density_list.append({
            "keyword": kw,
            "count": count,
            "density_percent": density
        })

    coverage = round(
        (sum(1 for d in density_list if d["count"] > 0) / len(jd_keywords)) * 100,
        2
    ) if jd_keywords else 0

    return {
        "keyword_density": density_list,
        "coverage_percent": coverage
    }