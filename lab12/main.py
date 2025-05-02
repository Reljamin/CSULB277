from tasklist import Tasklist
from check_input import get_int_range

def get_date():
    month = get_int_range("Enter month: ", 1, 12)
    day = get_int_range("Enter day: ", 1, 31)
    year = get_int_range("Enter year: ", 2000, 2100)
    return f"{month:02}/{day:02}/{year}"

def get_time():
    hour = get_int_range("Enter hour (0-23): ", 0, 23)
    minute = get_int_range("Enter minute (0-59): ", 0, 59)
    return f"{hour:02}:{minute:02}"

def main_menu():
    print("\n-Tasklist-")
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")
    return get_int_range("Enter choice: ", 1, 6)

def main():
    tasks = Tasklist()
    while True:
        print(f"\nTasks to complete: {len(tasks)}")
        choice = main_menu()

        if choice == 1:
            current = tasks.get_current_task()
            print(f"Current task is: {current}" if current else "All tasks are complete.")

        elif choice == 2:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        elif choice == 3:
            current = tasks.get_current_task()
            if current:
                print(f"Marking complete: {current}")
                tasks.mark_complete()
                new_current = tasks.get_current_task()
                print(f"New current task: {new_current}" if new_current else "All tasks are complete.")
            else:
                print("No tasks to complete.")

        elif choice == 4:
            desc = input("Enter a task description: ")
            date = get_date()
            time = get_time()
            tasks.add_task(desc, date, time)

        elif choice == 5:
            date = get_date()
            print(f"Tasks due on {date}:")
            found = False
            for task in tasks:
                if task.date == date:
                    print(task)
                    found = True
            if not found:
                print("No tasks found on that date.")

        elif choice == 6:
            print("Saving List...")
            tasks.save_file()
            break

if __name__ == "__main__":
    main()