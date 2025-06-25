from logger import log_usage, get_running_apps, run_auto_logger
from report import plot_daily_summary

def main():
    while True:
        print("\n=== Digital Minimalism Tracker ===")
        print("1. Log usage manually")
        print("2. View running apps")
        print("3. Start auto-logger")
        print("4. View daily graph")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            app = input("Enter app name: ")
            minutes = input("Enter time spent (in minutes): ")
            if minutes.isdigit():
                log_usage(app, int(minutes))
            else:
                print("Invalid input.")
        elif choice == "2":
            apps = get_running_apps()
            print("\n[Running Apps Detected]")
            for app in apps:
                print(f"- {app}")
        elif choice == "3":
            run_auto_logger()
        elif choice == "4":
            plot_daily_summary()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

