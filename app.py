import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd
import pytz

# Proper IST date
IST = pytz.timezone('Asia/Kolkata')
today = datetime.utcnow().astimezone(IST).date()
filename = "digital_usage.json"

def load_data():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f)

def get_dataframe(data, date_str):
    if date_str in data:
        df = pd.DataFrame(data[date_str], columns=["app", "minutes"])
        return df.groupby("app")["minutes"].sum().reset_index().rename(columns={"app": "App", "minutes": "Minutes"})
    return pd.DataFrame(columns=["App", "Minutes"])

st.set_page_config(page_title="Digital Minimalism Tracker", layout="centered")

# Logo + Title + Message
st.markdown(
    """
    <div style='text-align: center;'>
        <img src="https://raw.githubusercontent.com/ranahitesh07/Digital-Minimalism-Tracker/main/logo.png" width="120">
        <h1 style='margin-bottom: 0;'>Digital Minimalism Tracker</h1>
        <p style='font-size: 18px; color: gray;'>Track your daily browser usage and build better digital habits.</p>
    </div>
    """,
    unsafe_allow_html=True
)

data = load_data()

# Add Entry Form
with st.form("log_usage"):
    st.subheader(f"📝 Log Your App Usage (Today: {today})")
    app_name = st.text_input("App Name")
    minutes = st.number_input("Minutes Used", min_value=1)
    submitted = st.form_submit_button("Add Entry")
    if submitted and app_name:
        date_str = str(today)
        if date_str not in data:
            data[date_str] = []
        data[date_str].append([app_name, int(minutes)])
        save_data(data)
        st.success(f"Added {minutes} minutes to '{app_name}'.")

# Display Today's Usage
st.subheader(f"📊 Today's Usage ({today})")
df_today = get_dataframe(data, str(today))
if not df_today.empty:
    st.bar_chart(df_today.set_index("App"))
    st.dataframe(df_today)
else:
    st.info("No data logged yet for today.")

# Manage Today's Data
st.subheader("⚙️ Manage Today's Data")
col1, col2 = st.columns(2)

with col1:
    if st.button("🧹 Clear Today's Data"):
        if str(today) in data:
            del data[str(today)]
            save_data(data)
            st.warning("Today's data has been cleared.")

with col2:
    if st.button("➕ Create Empty Table for Today"):
        if str(today) not in data:
            data[str(today)] = []
            save_data(data)
            st.info("Empty table created for today.")

# Auto Tracking Placeholder
st.subheader("🔄 Coming Soon: Auto Tracking")
st.info("You'll soon be able to automatically track app usage without typing manually!")

# ✅ Footer
st.markdown("---")
st.markdown("<small>Made with Python and Streamlit</small>", unsafe_allow_html=True)
