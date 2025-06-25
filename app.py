import json
import os
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

st.title("📊 Digital Minimalism Tracker")

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
