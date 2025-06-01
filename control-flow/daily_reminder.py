# Get user inputs
Task = input("Enter your task: ").strip()
Time_Bound = input("Is it time-bound? (yes/no): ").lower().strip()
Priority = input("Priority (high/medium/low): ").lower().strip()


# Input validation
if Priority not in ["high", "medium", "low"] or Time_Bound not in ["yes", "no"]:
    print("Invalid input. Please enter a valid priority (high/medium/low) and time-bound status (yes/no).")
else:
    match Priority:
        case "high":
            if Time_Bound == "yes":
                print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{Task}' is a high priority task that should be completed as soon as possible after finishing time-bound tasks.")
        
        case "medium":
            if Time_Bound == "yes":
                print(f"Reminder: '{Task}' is a medium priority task that should be completed today after finishing high priority tasks.")
            else:
                print(f"Reminder: '{Task}' is a medium priority task that should be completed after high priority and time-sensitive tasks.")
        
        case "low":
            if Time_Bound == "yes":
                print(f"Reminder: '{Task}' is a low priority task. Consider completing it after medium priority tasks.")
            else:
                print(f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")
