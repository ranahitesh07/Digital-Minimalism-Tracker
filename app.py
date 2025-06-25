import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd
import pytz

# Timezone: India
IST = pytz.timezone('Asia/Kolkata')
today = datetime.now(IST).date()
filename = "digital_usage.json"

# Load or create data
def load_data():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f)

# Prepare DataFrame for selected date
def get_dataframe(data, date_str):
    if date_str in data:
        df = pd.DataFrame(data[date_str], columns=["app", "minutes"])
        return df.groupby("app")["minutes"].sum().reset_index().rename(columns={"app": "App", "minutes": "Minutes"})
    return pd.DataFrame(columns=["App", "Minutes"])

# Page layout
st.set_page_config(page_title="Digital Minimalism Tracker", layout="centered")

# ✅ Centered Logo + Title + Welcome message
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

# Add new usage entry
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

# Display today's usage
st.subheader(f"📊 Today's Usage ({today})")
df_today = get_dataframe(data, str(today))
if not df_today.empty:
    st.bar_chart(df_today.set_index("App"))
    st.dataframe(df_today)
else:
    st.info("No data logged yet for today.")

# View other days
st.subheader("📅 Check Another Day")
dates_available = sorted(data.keys(), reverse=True)
if dates_available:
    selected_date = st.selectbox("Select Date", dates_available)
    df_selected = get_dataframe(data, selected_date)
    if not df_selected.empty:
        st.bar_chart(df_selected.set_index("App"))
        st.dataframe(df_selected)
    else:
        st.warning("No data for this day.")

# Manage today's data
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

# Footer
st.markdown("---")
st.markdown("<small>Made with Python and Streamlit</small>", unsafe_allow_html=True)
