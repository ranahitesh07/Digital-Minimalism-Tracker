import json
import os
from datetime import datetime
import psutil
import time

DATA_FILE = "digital_usage.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def log_usage(app_name, minutes):
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in data:
        data[today] = []
    data[today].append({"app": app_name, "minutes": minutes})
    save_data(data)
    print(f"[+] Logged {minutes} minutes for '{app_name}'.")

def get_running_apps():
    allowed_keywords = [
        "chrome", "firefox", "edge", "opera", "brave",
        "code", "notepad", "sublime", "spotify",
        "word", "excel", "discord", "zoom",
        "teams", "whatsapp", "telegram"
    ]

    tracked_apps = set()
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name'].lower()
            for keyword in allowed_keywords:
                if keyword in name:
                    tracked_apps.add(name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError):
            continue

    return sorted(tracked_apps)

def run_auto_logger(interval_minutes=5):
    print(f"\n[Auto-Logger] Running... Press Ctrl+C to stop.")
    try:
        while True:
            apps = get_running_apps()
            if apps:
                print(f"\n⏱ Logging {len(apps)} app(s) at {datetime.now().strftime('%H:%M:%S')}")
                for app in apps:
                    log_usage(app, interval_minutes)
            else:
                print("[!] No trackable apps running.")
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("\n[Auto-Logger] Stopped by user.")
