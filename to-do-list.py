def pause(text):
    print(text)
    input()
def choose(valid_choices): 
    while True:
        choice = input("Enter your choice: ").upper()
        if choice in valid_choices:
            return choice
        print("Invalid choice")
def edit():
            new_task = input("Enter new task: ")
            with open("To-do-list.txt", "a") as save_file:
                save_file.write(new_task + "\n")
def createlist():
     with open("To-do-list.txt", "w") as f:
         pass
     task = " "
def openlist():
     try:
        with open("To-do-list.txt", "r") as save_file:
            data = save_file.read().splitlines()
            return data
     except FileNotFoundError:
         print("File not found! Starting from new file")
         createlist()
         return[]
print("""
A - Load existing list" 
B - Create New and overwrite""")
choice = choose(["A", "B"])
if choice == "A":
     tasks  = openlist()
     print(tasks)
if choice == "B":
     createlist()
print("""
Would you like to add new tasks
A -Yes, I want to edit
B- No, i want to change status of tasks
C - No, i want to view the list
""")
while choice != "C":
    choice = choose(["A" , "B" , "C"])
    if choice == "A":
        edit()
        print("Task added")
    if choice == "B":
        tasks = openlist()
        
        if not tasks:
            print("Your list is empty! Nothing to change.")
        else:
            print("\n--- Current Tasks ---")
            for index, task in enumerate(tasks):
                print(f"{index + 1} - {task}")
            
            valid_numbers = [str(i + 1) for i in range(len(tasks))]
            print("\nWhich task number would you like to change?")
            task_choice = int(choose(valid_numbers)) - 1
            
            # --- BUG FIX HERE ---
            # Check if "[DONE]" is already in the task text
            if "[DONE]" in tasks[task_choice]:
                print(f"'{tasks[task_choice]}' is already completed!")
                print("A - Leave it as done")
                print("B - Mark it as incomplete again")   
                sub_choice = choose(["A", "B"])
                if sub_choice == "B":
                    # .replace() removes the " [DONE]" text by replacing it with nothing
                    tasks[task_choice] = tasks[task_choice].replace(" [DONE]", "")
                    print("Task marked as incomplete!")
            else:
                # If it wasn't done, add the [DONE] tag normally
                tasks[task_choice] = tasks[task_choice] + " [DONE]"
                print("Task status updated successfully!")
            
            # Save everything back to the file
            with open("To-do-list.txt", "w") as save_file:
                for task in tasks:
                    save_file.write(task + "\n")
view_tasks = openlist()
print(view_tasks)