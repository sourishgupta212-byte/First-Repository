def get_choice(valid_choices):
    while True:
        choice = input("Enter your choice: ").upper()
        if choice in valid_choices:
           return choice
        print("invalid choice")
def display_menu():
    running = True
    while running:
     print("""
  A - Task manager
  B - Exit
    """)
     choice = get_choice(["A", "B"])
     if choice == "A":
        taskmanager()
     elif choice == "B":
        running = False
def createfile(file_name):
   with open (file_name, "w"):
      pass
   print("New file created!")
def additems(file_name, content):
 new_task = input(f"Enter your {content} :")
 with open (file_name ,"a") as task_file:
  task_file.write(new_task + "\n" )
def file_error(file_name):
 no_file = True
 print("No file found! Would you like to create a file?")
 print("""A - Create a file 
 B - Do not create a file""")
 choice = get_choice(["A", "B"])
 if choice == "A":
    createfile(file_name)
    displaylist(file_name)
    no_file = False
 if choice == "B":
    print("Okay your loss then")
    no_file = True
 return no_file
def displaylist(file_name):
    with open(file_name, "r") as task_file: 
       data = task_file.read().splitlines()
    for index, item in enumerate(data, start=1):
     print(f"{index} {item}")
    return data
def taskmanager():
    try:
     displaylist("task.txt")
    except FileNotFoundError:
        no_file = file_error("task.txt")
        while no_file:
         no_file = file_error("task.txt")
        displaylist("task.txt")
    running = True
    while running:
        print("""
What would you like to do?
A - Add new tasks
B - Edit existing tasks
C - Change status of tasks
D - exit
            """)
        choice = get_choice(["A", "B", "C", "D"])
        if choice == "A":
         additems("task.txt" , "task")
        elif choice == "B":
           print("Which task would you like to edit?")
display_menu()
# ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# I AM DYING
