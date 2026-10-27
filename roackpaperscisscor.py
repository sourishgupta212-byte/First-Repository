import random
def result(pick, opp_pick):
    print(f"""You picked: {pick}
Computer picked: {opp_pick}
 """)
tools = ["Rock", "Paper", "Scissor"]
while True:
    choice = input("Enter your choice: ").upper()
    if choice in ("ROCK" , "PAPER", "SCISSOR"):
        pick = choice
        break   
    print("Invalid choice")
opp_pick = random.choice[tools]
if pick == "ROCK":
    if opp_pick == "Rock":
        result("Rock", "Rock")
        print("It's a tie")
    if opp_pick == "Paper":
        result("Rock", "Paper")
        print("Computer won")
    if opp_pick == "Scissor":
        result("Rock")
        