def pause(text="Press Enter to continue..."):
    input(text)

def choose(valid_choices):
    while True:
        choice = input("Enter your choice: ").upper().strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")

def create_list():
    with open("To-do-list.txt", "w") as f:
        pass
    print("New empty list created.")

def open_list():
    try:
        with open("To-do-list.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print("File not found. Creating a new one.")
        create_list()
        return []

def save_list(tasks):
    with open("To-do-list.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("\nYour list is empty.")
    else:
        print("\n--- Current Tasks ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    new_task = input("Enter new task: ").strip()
    if new_task:
        tasks.append(new_task)
        save_list(tasks)
        print("Task added!")
    else:
        print("Task cannot be empty.")

def mark_done(tasks):
    if not tasks:
        print("Your list is empty!")
        return

    view_tasks(tasks)
    valid_numbers = [str(i) for i in range(1, len(tasks) + 1)]
    print("Which task number would you like to mark as completed?")
    choice = choose(valid_numbers)
    index = int(choice) - 1

    if "[DONE]" not in tasks[index]:
        tasks[index] = tasks[index] + " [DONE]"
        save_list(tasks)
        print("Task marked as completed!")
    else:
        print("That task is already marked as done.")

# ========== MAIN PROGRAM ==========
print("""
A - Load existing list
B - Create New and overwrite
""")
start_choice = choose(["A", "B"])

if start_choice == "A":
    tasks = open_list()
elif start_choice == "B":
    create_list()
    tasks = []

# Main menu loop
while True:
    print("""
--- MENU ---
A - Add new task
B - Mark task as completed
C - View the list
D - Exit
""")
    choice = choose(["A", "B", "C", "D"])

    if choice == "A":
        add_task(tasks)
    elif choice == "B":
        mark_done(tasks)
    elif choice == "C":
        view_tasks(tasks)
    elif choice == "D":
        print("Goodbye!")
        break

    pause()