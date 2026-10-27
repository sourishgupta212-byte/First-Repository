Last_name = "Smith"
def anony(text):
    pause("Anonymous:" + " " + (text))
Name = "Jhon"
full = Name + " " + Last_name
print(full)
name_characters = len(full)
print(name_characters - 1)
print(full.upper())
secret_name = (full.replace("Jhon", "David")) 
print(secret_name)
print ("David" in secret_name) 
print(secret_name.upper())
print(len(secret_name) + (float(3.4)))
print(len(secret_name) ** 1.5)
x = 10 
x /= 5
print(x + 5)
print(round(1.5))
print(abs(-5))
x = input("Enter your age: ")
if int(x) < 18:
    print("You are under 18. So congratulations! You are not allowed to vote.")
if int(x) >= 18:
    print("You are allowed to vote")
print("So uh i am pretty tired now. Like, I get it i learnt a A LOT of math functions but this is becoming 'OH LET US TEACH THIS RANDOM KID WIERD ASS STUFF")
if 10 == 10:
    print("WOW *CLAPS* yeah you dont know, but if this is getting printed, the code secretly ran a 'if 10 == 10' which allows this text to be printed. so yeah, it is useless")
print("""
So yeah, This is a large note so it will use triple quote instead of one
I am sort of practicting code right now i hope you dont mind
""")
print("Proccessing absolutely nothing....")
print("Btw remember to drink water")
print("Also check if your phone is using mobile data or WI-Fi")
print("Proccessing complete")
print("Creating function.....")
def pause(text):
    print(text)
    input()
print("Function extracted...")
print("Updating programme..")
print("Accessing private files..")
print("Selling private files..")
print("Making money..")
print("Ignoring user complaints..")
print("Update complete.")
print("Yoooo")
pause("New update, From now on, You can Press enter to make the line of code start. You control the pace Now")
pause("Now, I dont have much to say. I would like a bit of feedback, but there isn't anything useful here.")
pause("WAIT! I THINK WE CAN HAVE A GAME")
pause("Intiliziaing download.......")
pause("Looking through search history....")
pause("Feeling disgusted by searcg History..")
pause("Ignoring use complaints again...")
pause("Download : 86%")
pause("Dowload failed.")
pause("Wait, What?")
pause("This shoudn't happen")
pause("I need to look through the code, maybe i will find the cause of this")
pause("For now, Stay in this room AND DO NOT TOUCH ANYTHING!!")
pause("Transporting to room...")
pause("Arrival complete")
def choose(valid_choices):
    while True:
        choice = input(" ")
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice.")
anony("Psst..Over here")
anony("Here, Take this")
pause("Item Acquired :Key")
anony("There is a Door beind you. I know the narrator told you not to touch anything, but he CANNOT be trusted")
pause("*Noises*")
pause("Oh he is here! I must hide")
pause("Narrator: Hey! I am back. I was unable to find anything in the code for now. Just came back to check on you.")
pause("*About to leave*")
pause("Narrator: Before i go, Did anyone happen to give you a key")
pause("You : No?")
pause("Narrator: Good. If someone Offers you a key, Tell me immidiately. No one here can be trusted expect me")
pause("Narrator: *Leaves*")
pause("Anonymous: Hey! Come here. You need to leave right now. He is acting like he is friendly, but trust me, he is hiding his true idenity.")
pause("Anonymous: Here, Have this. It's a Listening device. It will allow me to connect through and talk to you at all times..mostly all times.")
pause("Now, he doesn't actually track you. You can look around the room. Try to search for anything useful in the room. you might find something")
pause("""
1. Search desk
2. Search Bookshelf
""")
searched = [] 
def search(place, result):
    if place in searched:
        pause("You already searched this.")
    else:
         pause(result)
         searched.append(place)
while True:
    if len(searched) == 2:
        break
    print("""
1. Search desk
2. Search bookshelf
""")
    choice = choose(["1", "2"])
    if choice == "1":
        search("Desk", "You searched the desk")
    if choice == "2":
        search("Bookshelf", "You searched the bookshelf")
pause("You: A Metal device from the desk. The bookshelf had a book named '1+1 equals purple or maybe seven: How i failed at maths but succedeed in game development")
pause("You: But i suppose that is not important")
pause("Anonymous:*inspects the device*")
anony("BRO this is not even a device it's a litreal metal scrap")
anony("JUST UNLOCK THE DOOR WITH THE KEY I GAVE YOU IT'S NOT SO HARD")
def nar(text):
    pause("Narrator:" + " " + (text))
def you(text):
    pause("You:" + " " + (text))
you("Okay fne i will open it!")
pause("Door:*UNLOCKS*")
you("WHY DOES THE DOOR HAVE A CHARACTER DIALOUGE")
def door(text):
    pause("Door:" + " " +(text))
door("Look, the narrator is away and SOMEONE HAS TO NARRATE!")
you("Fine. Now open")
door("*Opens dramatically*")
you("What is this place?")
door("A roo-")
you("SHUT UP!")
door(":(")
you("This seems to be an ordinary room")
door("Wait..did the wierd guy give you the key?")
you("Yeah, why?")
door("Well he can't exactly be trusted")
you("Why?")
door("I said i would narrate, not spoil the plot")
door("Suddenly, the wall in front of you fell down and a metal hallway with two doors was revealed...")
door("""
A - Go right
B- Go left
C- Ask the door what is happening
""")
def comp(text):
    pause("Computer: " + text)
def goright():
    door("You choose to go right..")
    door("As you get closer to the door, You see something wirtten on it")
    door("Computer terminal")
    you("Why does a out-of-code place have a computer terminal?")
    door("You open me- the door")
    door("inside, you see dozens upon dozens on computers lined up")
    door("All of them running some sort of program")
    door("you enter room")
    door("Upon entering, the door behind you closes")
    door("THUD")
    door("Scary")
    door("You see on of the operations")
    comp("Searching files..")
    comp("Updating files")
    comp("Update complete")
    comp("Searching files")
    comp("Updating files")
    door("And so on")
    you("Must be important")
    door("You eventually see a slightly open drawer")
    pause("""
    A - Look through the drawer
    B - Leave it alone""")
    choice = choose(["A", "B"])
    if choice == "A":
        door("You decide to look through the drawer")
        door('There, You see a Document named "Update Log"')
        you("Wait, So the system is update every minute?")
        you("That explains these computers")
        you("*Notices Red line*")
        you("What's this?")
        you(' "Game import failed" ')
    if choice == "B":
        door("You decide to move along")
    door('After Moving forward, you saw a door with "Exit" on it')
def goleft():
    door("you choose to go left")
choice = choose(["A" , "B" , "C"])
if choice == "A":
    goright()
if choice == "B":
    goleft()
if choice == "C":
    you("Mr.Door, What is this?")
    door("You were rude to me. Why should i tell you?")
    pause("""
     A - Apologize
     B - Continue anyway
     """)
    choice = choose(["A" , "B"])
    if choice == "A":
        you("I am sorry")
        you("Now please tell me what this is about")
        door("Well since you apologized")
        door("I will tell you")
        door("It is a hallway that leads to two different ways")
        you("...")
        you("Very helpful")
        pause("""
        A - Go right
        B- Go left""")
        choice = choose(["A", "B"])
        if choice == "A":
            goright()
        if choice == "B":
            goleft()
    if choice == "B":
        you("Nah I am not saying sorry")
        door("Suit yourself")
        pause("""
        A - Go right
        B- Go left""")
        choice = choose(["A", "B"])
        if choice == "A":
            goright()
        if choice == "B":
            goleft()
door("Meanwhile..Back at the original room")
nar("Hey! I am-")
nar("..")
nar("Where is the player?")
nar("Eren.")
nar("It's always eren")
nar("I am going to find you eren")
nar("And this time i am going to make sure you don't do this again")
