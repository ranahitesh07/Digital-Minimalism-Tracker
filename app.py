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
    if df.empty or "app" not in df.columns or "minutes" not in df.columns:
        return pd.DataFrame(columns=["App", "Minutes"])
    return df.groupby("app")["minutes"].sum().reset_index().rename(columns={"app": "App", "minutes": "Minutes"})

st.set_page_config(page_title="Digital Minimalism Tracker", layout="centered")

# ─── Logo and Title ─────────────────────────────────────────────
st.markdown("""
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/ranahitesh07/Digital-Minimalism-Tracker/main/logo.png' width='150'>
        <h1 style='color: #3E64FF;'>Digital Minimalism Tracker</h1>
    </div>
""", unsafe_allow_html=True)

# ─── Load Data ─────────────────────────────────────────────

data = load_data()
today = datetime.now().strftime("%Y-%m-%d")
if today not in data:
    data[today] = []
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ─── Log Usage Form (Placed at top) ────────────────────────
st.markdown("---")
st.subheader("📥 Log Your App Usage (Today)")

with st.form("log_usage_form"):
    app_name = st.text_input("App Name")
    minutes = st.number_input("Minutes Spent", min_value=1, step=1)
    submitted = st.form_submit_button("Submit")

    if submitted:
        if app_name.strip() == "":
            st.error("Please enter a valid app name.")
        else:
            data[today].append({"app": app_name.lower(), "minutes": minutes})
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)
            st.success(f"Logged {minutes} min for '{app_name}'")
            st.rerun()

# ─── Default View for Today ────────────────────────────────

st.markdown("---")
st.subheader(f"📊 Today's Usage ({today})")

df_today = get_dataframe(data, today)
if df_today.empty:
    st.info("No data logged yet for today.")
else:
    st.bar_chart(df_today.set_index("App"))
    with st.expander("📄 View Table"):
        st.dataframe(df_today)
    csv = df_today.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Today's CSV", csv, f"{today}_usage.csv", "text/csv")

# ─── Select Other Date ─────────────────────────────────────

st.markdown("---")
st.subheader("📅 Check Another Day")
dates = sorted(data.keys(), reverse=True)
selected_date = st.selectbox("Select Date", dates, index=0)
if selected_date != today:
    df = get_dataframe(data, selected_date)
    if df.empty:
        st.info("No data for this day.")
    else:
        st.bar_chart(df.set_index("App"))
        with st.expander("📄 View Table"):
            st.dataframe(df)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", csv, f"{selected_date}_usage.csv", "text/csv")

# ─── Manage Today's Data ───────────────────────────────────

st.markdown("---")
st.subheader("⚙️ Manage Today's Data")

col1, col2 = st.columns(2)

with col1:
    if st.button("🧹 Clear Today's Data"):
        data[today] = []
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        st.success("Today's data cleared.")
        st.rerun()

with col2:
    if st.button("➕ Create Empty Table for Today"):
        if today not in data:
            data[today] = []
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)
            st.success("Empty entry created for today.")
            st.rerun()
        else:
            st.warning("Today's entry already exists.")