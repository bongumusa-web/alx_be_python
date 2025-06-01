# Get user inputs
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is this time-bound? (yes/no): ").lower().strip()

# Input validation
if priority not in ["high", "medium", "low"] or time_bound not in ["yes", "no"]:
    print("Invalid input. Please enter a valid priority (high/medium/low) and time-bound status (yes/no).")
else:
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task that should be completed as soon as possible after finishing time-bound tasks.")
        
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be completed today after finishing high priority tasks.")
            else:
                print(f"Reminder: '{task}' is a medium priority task that should be completed after high priority and time-sensitive tasks.")
        
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task. Consider completing it after medium priority tasks.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
