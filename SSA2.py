def pause(text):
    print(text)
    input()
def get_choice(valid_choices):
    while True:
        choice = input("Enter your choice: ").upper()
        if choice in valid_choices:
            return choice
        print("Invalid choice")
def save_game(checkpoint):
    with open("SSA2_save", "a") as save_file:
     save_file.write(checkpoint)
def open_save():
    with open("SSA2_save" , "r") as save_file:
     save =  save_file.read()
     return save
def create_save():
   with open("SSA2_save" , "w") as save_file:
      pass
def you(text):
     print(f"You: {text}")
     input()
def principal(text):
     print(f"Principal: {text}")
     input()
stats = {
    "teacher_approval" : 65,
    "student_approval": 40,
    "influence" : 50,
    "goat_popularty" : 60,
    "stability" : 40,
    "SRP standing" : 20,
    "friend_popularity" : 40
}
pause("In your school...")
pause("The adminstration and Principal was facing heavy critisism")
pause("They were making decisions without any student input or involvement")
pause("Exhuasted by the faliures of decisions and policies, the principal decided to form a student position ")
pause("The Name of the position will be 'The Supreme Student Administrator")
pause('The Principal, seeing your excellent academic record, appointed you as SSA "until further notice"')
pause("You did not ask for it. Yet here you were, as  the Supreme student adminstrator")
pause("You are told to meet the prinicpal for a small briefing")
pause("You walk into the office, and there you see the prinicpal sitting")
you("Good morning Sir")
principal("Sit down. You are the new SSA, since you had a great record. i wanted to reward you ")
principal("The powers of thee SSA are poorly defined, but you are responsible for handling student issues and report to the office")
principal("Good luck")