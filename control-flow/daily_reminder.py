task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is this time-bound? (yes/no): ").lower()

match task:
     case _ if priority == "high" and time_bound == "yes":
           print(f"Reminder: {task} is a high priority task that requires immediate attention today")
     case _ if priority == "medium" and  time_bound == "yes":
           print(f"Reminder: {task} is a medium priority task that should be completed today after fininshing high priority tasks") 
     case _ if priority == "low" and time_bound == "yes":
            print(f"Reminder: {task} is a low priority task. consider completing it when you have completed the medium priotiy tasks.")
     case _ if priority == "high" and time_bound == "no":
              print(f"Reminder: {task} is a high priority task that should be completed as soon as possible after fininshing time-bound tasks")
     case _ if priority == "medium" and time_bound == "no":
              print(f"Reminder: {task} is a medium priority task that should be completed after fininshing high priority tasks and time-bound medium priority tasks")
     case _ if priority == "low" and time_bound == "no":
                print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
     case _ if priority not in ["high", "medium", "low"] or time_bound not in ["yes", "no"]:
            print("Invalid input. Please enter a valid priority (high/medium/low) and time-bound status (yes/no).")