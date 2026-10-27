def nar(text):
    print("Narrator:" + " " + (text))
    input()
def pause(text):
    print(text)
    input()
def choose(valid_choices):
    while True:
        choice = input("Enter your Choice: ")
        if choice in valid_choices:
            return choice
nar("Steve worked in a office in a big building")
nar("He even had his own little room with his own cubicle")
nar("His Job was very simple")
nar("Orders came to him, telling him what button to puch on a keyboard and when")
nar("Orders came, and he pushed buttons")
nar("Steve was happy")
nar("One day, Orders stopped coming")
nar("He waited")
nar("No one even stopped to say hi!")
nar("He decides to leave the room")
nar("1. Leave the room")
Choice = choose(1)
nar("After stepping out, He sees that all of his Co-workers were gone")
nar("Perhaps he had missed a meeting")
nar("He moved forward towards the meeting room with two doors")
nar("Steve went right, towards the meeeting room ")
nar("""
A - Go right
B - Go left 
""")
Choice = choose([1, 2])