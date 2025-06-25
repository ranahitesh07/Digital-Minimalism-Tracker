import json
import os
from datetime import datetime
from PIL import Image
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

DATA_FILE = "digital_usage.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def get_dataframe(data, selected_date):
    if selected_date not in data:
        return pd.DataFrame(columns=["App", "Minutes"])
    day_data = data[selected_date]
    df = pd.DataFrame(day_data)
    return df.groupby("app")["minutes"].sum().reset_index().rename(columns={"app": "App", "minutes": "Minutes"})

st.set_page_config(page_title="Digital Minimalism Tracker", layout="centered")

# ─── Logo and Title ─────────────────────────────────────────────
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/ranahitesh07/Digital-Minimalism-Tracker/main/logo.png' width='150'>
        <h1 style='color: #3E64FF;'>Digital Minimalism Tracker</h1>
    </div>
""", unsafe_allow_html=True)

# ─── Main Content ─────────────────────────────────────────────

data = load_data()
dates = sorted(data.keys(), reverse=True)

if not dates:
    st.warning("No usage data available yet.")
else:
    selected_date = st.selectbox("Select Date", dates)
    df = get_dataframe(data, selected_date)

    if df.empty:
        st.info("No data for the selected day.")
    else:
        st.subheader(f"Usage for {selected_date}")
        st.bar_chart(df.set_index("App"))

        with st.expander("📄 View Table"):
            st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", csv, f"{selected_date}_usage.csv", "text/csv")

st.markdown("---")
st.subheader("📥 Log New App Usage")

with st.form("log_usage_form"):
    app_name = st.text_input("App Name")
    minutes = st.number_input("Minutes Spent", min_value=1, step=1)
    submitted = st.form_submit_button("Submit")

    if submitted:
        if app_name.strip() == "":
            st.error("Please enter a valid app name.")
        else:
            today = datetime.now().strftime("%Y-%m-%d")
            if today not in data:
                data[today] = []
            data[today].append({"app": app_name.lower(), "minutes": minutes})

            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)

            st.success(f"Logged {minutes} min for '{app_name}'")
            st.rerun()