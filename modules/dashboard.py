import pandas as pd
import streamlit as st
import altair as alt


def render_dashboard():

    try:
        df = pd.read_csv("output/candidate_scores.csv")
    except FileNotFoundError:
        st.warning("No candidate data available yet.")
        return

    if df.empty:
        st.warning("CSV exists but has no data.")
        return

    # -----------------------------
    # CLEAN MATCH SCORE COLUMN
    # -----------------------------
    df["match_score"] = (
        df["match_score"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["match_score"] = pd.to_numeric(df["match_score"], errors="coerce")

    df["coverage_percent"] = pd.to_numeric(
        df["coverage_percent"], errors="coerce"
    )

    df = df.dropna(subset=["match_score"])

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    total_candidates = len(df)
    avg_score = df["match_score"].mean()
    avg_ats = df["coverage_percent"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Candidates", total_candidates)

    with col2:
        st.metric("Average Match Score", round(avg_score, 1))

    with col3:
        st.metric("Average ATS Coverage", round(avg_ats, 1))

    st.divider()

    # -----------------------------
    # MATCH SCORE HISTOGRAM
    # -----------------------------
    st.subheader("Candidate Match Score Distribution")

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X(
                "match_score:Q",
                bin=alt.Bin(maxbins=10),
                title="Match Score"
            ),
            y=alt.Y("count()", title="Candidates"),
            color=alt.value("#4F46E5"),
        )
    )

    st.altair_chart(chart, use_container_width=True)

    st.divider()

    # -----------------------------
    # ATS COVERAGE TREND
    # -----------------------------
    st.subheader("ATS Coverage Trend")

    df["row_index"] = range(1, len(df) + 1)

    trend = (
        alt.Chart(df)
        .mark_line(point=True)
        .encode(
            x="row_index",
            y="coverage_percent",
            color=alt.value("#22C55E"),
        )
    )

    st.altair_chart(trend, use_container_width=True)

    st.divider()

    # -----------------------------
    # DATA TABLE
    # -----------------------------
    st.subheader("Candidate Evaluation Table")

    st.dataframe(df, use_container_width=True)