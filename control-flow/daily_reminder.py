# daily reminder .py
#prompt for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority taask."
    case _:
        reminder = "Invalid priority level entered. Please use high, medium, or low."
if priority in ["high", "medium", "low"]:
    if time_bound == "yes":
        reminder += "It requires immediate attention today!"
    elif time_bount == "no":
        reminder += "consider completing it when you have free time."
print(f"Reminder: {task_name} | Priority: {priority} | Immediate action required: {time_sensitive}")
