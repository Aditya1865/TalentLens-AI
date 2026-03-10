import streamlit as st
import tempfile
import pandas as pd

from modules.resume_parser import extract_text
from modules.text_preprocessor import clean_text
from modules.ai_evaluator import evaluate_candidate
from modules.report_generator import append_to_csv
from modules.dashboard import render_dashboard
from modules.ats_keyword_analyzer import (
    extract_jd_keywords,
    compute_keyword_density
)

st.set_page_config(page_title="TalentLens AI", layout="wide")

st.title("TalentLens AI — Intelligent Candidate Evaluation")
st.markdown(
    "<p style='font-size:18px;'>AI-powered resume intelligence platform.</p>",
    unsafe_allow_html=True,
)

tab1, tab2 = st.tabs(["🏆 Candidate Evaluation", "📊 Dashboard"])

# ---------------------------------------------------
# TAB 1
# ---------------------------------------------------

with tab1:

    st.header("Upload Resume for Evaluation")

    uploaded_file = st.file_uploader(
        "Select resume file",
        type=["pdf", "docx", "txt"]
    )

    jd_text = st.text_area(
        "Paste Job Description (JD)",
        height=180
    )

    if st.button("Run Evaluation"):

        if not uploaded_file or not jd_text.strip():
            st.error("Please upload resume and paste JD.")
            st.stop()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=uploaded_file.name
        ) as tmp:

            tmp.write(uploaded_file.read())
            resume_text = extract_text(tmp.name)

        cleaned_resume = clean_text(resume_text)

        jd_keywords = extract_jd_keywords(jd_text)

        ats_report = compute_keyword_density(
            cleaned_resume,
            jd_keywords
        )

        try:
            result_data = evaluate_candidate(
                cleaned_resume,
                jd_text
            )
        except Exception as e:
            st.error(str(e))
            st.stop()

        st.subheader("AI Evaluation")
        st.json(result_data)

        st.subheader("ATS Keyword Density Report")
        st.write(ats_report)

        st.subheader("Density Visualization")

        if "keyword_density" in ats_report:
            df = pd.DataFrame(ats_report["keyword_density"])

            if not df.empty:
                st.bar_chart(
                    df.set_index("keyword")["density_percent"]
                )

        append_to_csv(result_data, ats_report)

        st.success("Saved to CSV")

# ---------------------------------------------------
# TAB 2
# ---------------------------------------------------

with tab2:
    render_dashboard()