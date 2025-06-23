# Digital Minimalism Tracker - Simple Version
# Save this as tracker.py

import json
from datetime import datetime

# Configuration
DATA_FILE = "digital_usage.json"

def load_data():
    """Load tracking data from file"""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    """Save tracking data to file"""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def log_activity():
    """Record a new digital activity"""
    today = datetime.now().strftime('%Y-%m-%d')
    activity = input("\nWhat digital activity are you tracking? (e.g. Instagram, YouTube): ")
    minutes = int(input("How many minutes did you spend? "))
    
    data = load_data()
    
    if today not in data:
        data[today] = []
    
    data[today].append({
        "activity": activity.lower(),
        "minutes": minutes,
        "time": datetime.now().strftime('%H:%M')
    })
    
    save_data(data)
    print(f"✓ Logged {minutes} minutes of {activity}")

def daily_report():
    """Show today's digital usage summary"""
    data = load_data()
    today = datetime.now().strftime('%Y-%m-%d')
    
    if today not in data or not data[today]:
        print("\nNo activities logged today")
        return
    
    print("\n📱 Today's Digital Usage:")
    print("=" * 30)
    
    total = 0
    activities = {}
    
    for entry in data[today]:
        activity = entry["activity"]
        minutes = entry["minutes"]
        total += minutes
        activities[activity] = activities.get(activity, 0) + minutes
    
    for activity, minutes in activities.items():
        print(f"- {activity.title()}: {minutes} minutes")
    
    print(f"\nTotal screen time today: {total} minutes")
    print("=" * 30)

def main_menu():
    """Display the main menu"""
    print("\nDigital Minimalism Tracker")
    print("1. Log Activity")
    print("2. View Today's Report")
    print("3. Exit")

def main():
    """Main program loop"""
    print("\n=== Digital Minimalism Tracker ===")
    print("Track your digital habits mindfully\n")
    
    while True:
        main_menu()
        choice = input("\nChoose an option (1-3): ")
        
        if choice == '1':
            log_activity()
        elif choice == '2':
            daily_report()
        elif choice == '3':
            print("\nKeep practicing digital mindfulness! Goodbye.")
            break
        else:
            print("Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()
