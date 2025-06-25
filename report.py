import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

DATA_FILE = "digital_usage.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        print("[!] No data file found.")
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def plot_daily_summary():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    if today not in data:
        print(f"[!] No data for today ({today}).")
        return

    usage = {}
    for entry in data[today]:
        app = entry["app"]
        minutes = entry["minutes"]
        usage[app] = usage.get(app, 0) + minutes

    if not usage:
        print("[!] No usage logged for today.")
        return

    apps = list(usage.keys())
    times = list(usage.values())

    plt.figure(figsize=(10, 6))
    plt.bar(apps, times, color='skyblue')
    plt.xlabel("Apps")
    plt.ylabel("Time Spent (minutes)")
    plt.title(f"Digital Usage Summary for {today}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
