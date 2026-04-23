import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Chinese Banks Financial Dashboard", layout="wide")

st.title("🏦 Chinese Listed Banks Financial Performance")
st.markdown("2020–2024 | Data Source: WRDS / CSMAR")

@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "fs_bcombas_enhanced_with_metrics.csv"

    if not csv_path.exists():
        st.error(
            f"Data file not found: {csv_path}\n"
            "Please ensure the file exists at: ./data/fs_bcombas_enhanced_with_metrics.csv"
        )
        st.stop()

    df = pd.read_csv(csv_path)

    # Data cleaning
    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    for c in ["ROE", "Debt_to_Asset_Ratio", "Asset_Scale_Trillion"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    return df

df = load_data()

# Check required columns
required_cols = ["Company_name", "Year", "ROE", "Debt_to_Asset_Ratio", "Asset_Scale_Trillion"]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    st.error(f"Missing required columns: {missing}")
    st.stop()

st.sidebar.header("Filter")
banks = sorted(df["Company_name"].dropna().unique())
selected_bank = st.sidebar.selectbox("Select a Bank", banks)

bank_df = df[df["Company_name"] == selected_bank].sort_values("Year")

col1, col2 = st.columns(2)

with col1:
    st.subheader("ROE Trend")
    fig = px.line(
        bank_df, x="Year", y="ROE", markers=True,
        title=f"{selected_bank} - ROE (%)"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Debt-to-Asset Ratio Trend")
    fig2 = px.line(
        bank_df, x="Year", y="Debt_to_Asset_Ratio", markers=True,
        title=f"{selected_bank} - Debt-to-Asset Ratio (%)"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Key Metrics")
col3, col4, col5 = st.columns(3)

avg_roe = bank_df["ROE"].mean()
avg_dar = bank_df["Debt_to_Asset_Ratio"].mean()
avg_assets = bank_df["Asset_Scale_Trillion"].mean()

col3.metric("Avg ROE", "-" if pd.isna(avg_roe) else f"{avg_roe:.2f}%")
col4.metric("Avg Debt-to-Asset", "-" if pd.isna(avg_dar) else f"{avg_dar:.2f}%")
col5.metric("Avg Total Assets (Trillion CNY)", "-" if pd.isna(avg_assets) else f"{avg_assets:.2f}")