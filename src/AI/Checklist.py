# 1. Start of the day: Create the initial checklist
checklist = ["Exercise", "Read 10 pages", "Write code", "Buy groceries", "Clean room"]

# Initialize empty lists for the end-of-day review
completed_tasks = []
incomplete_tasks = []

print("--- End of Day Review ---")

# 2. Review each task in the checklist
for task in checklist:
    # Ask the user if the task was finished
    status = input(f"Did you finish '{task}'? (yes/no): ").lower()

    if status == 'yes':
        # Move to completed tasks
        completed_tasks.append(task)
    else:
        # Move to incomplete tasks
        incomplete_tasks.append(task)

# 3. Final Overview
print("\n" + "=" * 20)
print("DAILY SUMMARY")
print("=" * 20)

print(f"Completed Tasks: {completed_tasks}")
print(f"Incomplete Tasks: {incomplete_tasks}")

if not incomplete_tasks:
    print("\nAmazing! You finished everything today! 🎉")
else:
    print(f"\nYou have {len(incomplete_tasks)} tasks to carry over to tomorrow.")