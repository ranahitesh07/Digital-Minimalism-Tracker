
<p align="center">
  <img src="logo.png" alt="Digital Minimalism Tracker Logo" width="150"/>
</p>

<h1 align="center">Digital Minimalism Tracker</h1>

<p align="center">
  ⏱️ A clean and interactive Streamlit dashboard to manually log and visualize daily screen time.<br>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
</p>
<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python 3.10+"></a>
  <a href="https://digital-minimalism-tracker-alt.streamlit.app/">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit"/>
  </a>
  <a href="https://github.com/ranahitesh07/Digital-Minimalism-Tracker">
    <img src="https://img.shields.io/github/last-commit/ranahitesh07/Digital-Minimalism-Tracker" alt="Last Commit"/>
  </a>
  <a href="https://github.com/ranahitesh07/Digital-Minimalism-Tracker/stargazers">
    <img src="https://img.shields.io/github/stars/ranahitesh07/Digital-Minimalism-Tracker?style=social" alt="GitHub Stars"/>
  </a>
</p>

---

## 🔥 Live Demo

👉 [Launch the Web App](https://digital-minimalism-tracker-alt.streamlit.app/)

---

## ✨ Features

- ✅ Web-based manual logging of screen time
- 📊 Visualize app usage per day with charts
- 💾 Download usage data as CSV
- ➕ Create empty table for today
- 🧹 Clear today’s data with one click
- ☁️ Deployed on Streamlit Cloud

---

## 🗂️ Project Structure

```
Digital-Minimalism-Tracker/
├── app.py                 # Streamlit web dashboard
├── logger.py              # CLI logging script (optional)
├── main.py                # CLI interface (optional)
├── report.py              # CLI graph script (optional)
├── digital_usage.json     # Screen time data (JSON format)
├── logo.png               # App logo
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/ranahitesh07/Digital-Minimalism-Tracker.git
cd Digital-Minimalism-Tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app locally

```bash
streamlit run app.py
```

---

## 📋 Menu Options (Web Dashboard)

- 🔽 Select date to view usage
- 📊 View daily app usage in bar chart
- 📥 Download current day as CSV
- 📝 Manually log new app + time
- ➕ Create empty entry for today
- 🧹 Clear all logs for today

---

## 🧠 Ideas for Future

- Weekly usage trends
- App categorization (Productive / Distracting)
- Reminders or usage limits
- Multi-user tracking with login

---

## 📄 License

MIT License

---

## 🙌 Acknowledgement

Built to promote mindful digital habits and inspired by Digital Minimalism by Cal Newport.
