def pause(text):
    print(text)
    input()
def get_choice(valid_choices):
     while True:
            choice = input("Choice: ").upper()
            if choice in valid_choices:
                return choice
            print("Invalid choice.")
pause("You are an ordinary student.")
pause("A Completely average student")
pause("An Incredibly average student")
pause("In fact, if there were a competition for being average, you would probably finish somewhere in the middle.")
pause("Unfortunately")
pause("You are also the protagonist")
pause("Which means your peaceful existence is about to be ruined.")
pause("Three days later...")
pause("The Principal announces Student president election")
pause("Will you get involved?")
choice = input("Y/N: ").upper()
if choice == "N":
     print("like why-")
     pause("Do you not realize this is a political game")
     pause("I am picking yes for you. Live with it")
pause("You decide to get involved in the election")
pause("After waiting for a day, you learn that there is only one serious party looking for members")
pause("The Goat Group")
pause("It is based around the goat")
pause("A wise animal that wandered into the school playground yesterday")
pause("The group wants to run the goat as a official candiate")
pause("Although there might be a chance for you or any human to run if the school administration makes the goat disqualified")
pause("You stare at the poster of the goat group")
pause("The poster stares back.")
pause("The goat looks surprisingly confident.")
pause("You are beginning to suspect that nobody involved in this campaign is entirely sane.")
pause("You approach the party booth anyway")
pause('"Hello! will you like to join" ')
pause("After deciding this is probably not a cult, you say:")
pause('"Yeah, I would like to join."')
pause('He says that you might need to a more volunteer work first to get a offical memebership')
pause('Will you do volunteer work?')
choice = input('Y/N: ').upper()
if choice == "N":
     pause("*sighs*")
     pause("Look, i am trying to get you into politics. ABIDE BY IT")
pause("You are hesitant but agree.")
pause("You first task is: Poster work")
hardliner_strength = 35
hardliner_support = 40
hardliner_loyalty = 20
idealist_strength = 40
idealist_support = 35
idealist_loyalty = 20
moderate_strength = 25
moderate_support = 25
moderate_loyalty = 20
pause("You have multiple designs")
pause("You can only get one printed and paste it beacuse the printer guy is a jerk")
pause("What kind of posters will you put up?")
print("A-Put up GAINT goat posters")
print("B-Make the goat the main symbol with the party promises")
print("C-Make the goat the party branding, but mostly have party promises")
choice = get_choice(["A","B","C"])
if choice == "A":
     pause("You put up posters with GAINT goats")
     pause("The Goat lovers like this idea, but less than the goat itself")
     pause("Several students stop to admire the goat.")
     pause("One student asks if the goat is running for President.")
     pause("Technically, yes.")
     hardliner_strength += 1
     hardliner_loyalty +=2 
     hardliner_support +=5 
if choice == "B":
     pause("You put up posters with goats and party promises")
     pause("Yet the goat remains the main symbol")
     pause("Students seem interested in the promises.")
     pause("The goat still receives most of the attention.")
     idealist_loyalty += 2 
     idealist_strength += 1
     idealist_support += 5
if choice == "C":
     pause("You make a poster with mostly party promises")
     pause("You add a few recognizable party goat symbols")
     pause("A teacher compliments the professionalism of the poster.")
     pause("A Hardliner later asks where most of the goat went.")
     moderate_strength += 1
     moderate_loyalty += 2
     moderate_support += 5
pause('Party booth guy: "Ay you did fine." ')
pause('You, with glimmer of hope in your eyes: "Do i become a member now?"')
pause('Party booth guy: "NO, do more work"')
pause('You:"UGH" ')
print("You are asked to help recruit new volu-")
pause("Members")
pause('"Recruit one."')
pause('"One person?"')
pause('"One person."')
pause('"That seems easier."')
pause('"You would be surprised."')
pause("Who do you approach?")
print("A- Class topper. An intellectual")
print("B- Dumb guy, An meme-lover")
print("C- Average student")
choice = get_choice(["A","B","C",])
if choice == "A":
     pause("You approach the class topper.")
     pause('"Why should I join?"')
     pause('"What are your policies?"')
     pause('*explains policies*')
     pause(' "Hmmm. i might consider it" ')
     pause("Your task requirement is completed.")
     pause("You feel surprised why no one approached you")
     pause("Then you didn't approach the average student either")
     moderate_support += 2
     moderate_strength += 2
     moderate_loyalty += 5
if choice == "B":
     pause("You approach a student wearing a goat sticker.")
     pause('"GOAT!"')
     pause('"Goat."')
     pause('"GOAT!"')
     pause("You ask him to join")
     pause("HE agrees with the goat")
     pause("Unsuprisingly easy")
     hardliner_support += 2
     hardliner_strength += 2
     hardliner_loyalty += 5
if choice == "C":
     pause("You approach an ordinary student.")
     pause('"The goat is funny."')
     pause('"But what does the group actually want?"')
     pause("You explain the Party promises and the goat")
     pause("The student says he will consider joining")
     pause("Clearly the same thought process as you")
     idealist_support += 2
     idealist_strength += 2
     idealist_loyalty += 5
pause("The Party Booth Guy approaches you.")
pause('"Good news."')
pause('"You are almost a member."')
pause('"Really?"')
pause('"No."')
pause('"You have one final task."')
pause('"I swear."')
pause("Before he can tell you the task")
pause("Several new members arrive.")
pause("They immediately begin arguing about what the party actually stands for.")
pause("The Party Booth Guy points at you.")
pause('"Fix this."')
pause('"Why me?"')
pause('"Because I walked away first."')
pause("What do you say to them?")
pause("A - Emphasize loyalty to the Goat.")
pause("B - Emphasize reform through the Goat.")
pause("C - Emphasize practical student issues.")
choice = get_choice(["A","B","C"])
if choice == "A":
     pause("You explain that the Goat is the heart of the movement.")
     pause("Several members cheer.")
     pause("One member begins chanting for the Goat.")
     pause("You decide not to ask what the plan is after that.")
     hardliner_support += 3
     hardliner_strength += 3
     hardliner_loyalty += 6
if choice == "B":
     pause("You explain that the Goat brought everyone together.")
     pause("But real change is the ultimate goal.")
     pause("Several members nod in agreement.")
     pause("The argument becomes noticeably more productive.")
     idealist_support += 3
     idealist_strength += 3
     idealist_loyalty += 6
if choice == "C":
     pause("You explain that students joined because they want improvements.")
     pause("The Goat helped attract attention.")
     pause("But the party must have practical goals.")
     pause("Several members agree.")
     pause("One Hardliner looks mildly offended.")
     moderate_support += 3
     moderate_strength += 3
     moderate_loyalty += 6
pause("The Party Booth Guy returns.")
pause("The new members seem calmer.")
pause('"Good work."')
pause('"Can I become a member now?"')
pause('"Yes."')
pause('"Wait, really?"')
pause('"Yes."')
pause('"...That actually worked?"')
pause('"Congratulations. You are now an official member of the Goat Group."')
pause("The next morning...")
pause("An emergency announcement is made.")
pause('"The Goat has been officially disqualified from running for Student President."')
pause("...")
pause("An emergency meeting is called.")
pause("You attend.")
pause("The Goat Group falls silent.")
pause("For approximately three seconds.")
pause("Then everybody starts arguing.")
pause('"I TOLD YOU ALL! THE GOAT IS NOT A REAL CANDIDATE! THE ADMINISTRATION DID WHAT WAS ALWAYS GOING TO HAPPEN!"')
pause("says the Moderate leader.")
pause('"NO! THE GOAT WAS THE CANDIDATE, IS THE CANDIDATE, AND SHALL REMAIN THE CANDIDATE!"')
pause("replies the Hardliner leader.")
pause('"Regardless, we must announce a human candidate. We knew this day would come."')
pause("says the Idealist leader.")
pause('"WE DO NOT AGREE! WE SHALL NEGOTIATE WITH THE ADMINISTRATION!"')
pause("declares the Hardliner leader while several supporters begin chanting about goats.")
pause('"Then let us put it to a vote."')
pause("The Idealists agree immediately.")
pause("The Moderates agree immediately.")
pause("The Hardliners agree after several more goat chants.")
pause("A vote is called.")
pause("The future of the movement now hangs in the balance.")
pause("Cast your vote")
print("A - Support the Hardliners")
print("B - Support a Human Candidate")
hardliner_vote = False
human_candidate_vote  = False
choice = get_choice(["A","B"])
if choice == "A":
    hardliner_vote = True
    hardliner_loyalty += 20
    pause("You support the hardliner")
if choice == "B":
    human_candidate_vote = True
    moderate_loyalty += 20
    idealist_loyalty += 10
    pause("You support a human candidate")
hardliner_votes = hardliner_strength
human_votes = idealist_strength + moderate_strength
pause("The votes are counted...")
pause(f"Hardliner Votes: {hardliner_votes}")
pause(f"Human Candidate Votes: {human_votes}")
if hardliner_votes > human_votes:
    pause("The proposal fails.")
    pause("The Goat remains the official candidate until negotiations with the principal conclude")
elif human_votes > hardliner_votes:
    pause("The proposal passes.")
    pause("The party will nominate a human candidate.")
    pause('"IF THE GOAT IS SIDELINED, WE WILL LEAVE THE MOVEMENT!"')
    pause("Several Hardliners cheer.")
    pause("Several Idealists roll their eyes.")
    pause("The Moderates look surprisingly unsurprised.")
    hardliner_strength
else:
    pause("The vote is tied.")
    pause("Nobody expected this.")
    pause("Everybody starts arguing again.")

pause( "a Human candidate will be appoitned soon")
pause("For now you are asked to assist in organization of a rally")
pause("When you arrive, you see several members arguing")
pause("They belong to diffferent factions.")
pause("The Arugment is over the theme of the rally")
pause("Who will you support?")
print ("A - Simply goat rally and speech")
print ("B- Full of goats")
print("C- Barely any goats, and more speeches and agenda")
choice = get_choice(["A","B","C"])
if choice == "A":
     print ("You decide the party should choose a more standard rally")
     print("With your support, a Idealist controlled rally is done")
     idealist_loyalty += 5
     idealist_strength += 2
     idealist_support += 6
if choice == "B":
     pause("You decide that the party should not drift away from it's core prinicpals")
     pause("With you support, a Hardliner rally is done")
     hardliner_strength += 2
     hardliner_loyalty += 5
     hardliner_support += 6
if choice == "C":
     pause("You decide the goat doesn't win votes")
     pause("With your support, a Moderate rally is done")
     moderate_loyalty += 5
     moderate_strength += 2
     moderate_support += 6
pause("After the rally...")
pause("The week ends")
pause("Next week, a canidate will be choosen")
pause("You hope to run for Student President")
pause("However, getting nominated will be more difficult than winning the election ")
print("=================")
print("Week one complete")
print("=================")
print("Week Two")
def committee():

    total_strength = (
        hardliner_strength +
        idealist_strength +
        moderate_strength
    )

    hardliner_committee = round(
        hardliner_strength / total_strength * 100
    )

    idealist_committee = round(
        idealist_strength / total_strength * 100
    )

    moderate_committee = (
        100 -
        hardliner_committee -
        idealist_committee
    )

    pause("CURRENT PARTY COMMITTEE")

    print("Hardliners:", hardliner_committee, "votes")
    print("Idealists:", idealist_committee, "votes")
    print("Moderates:", moderate_committee, "votes")
committee()
import random

def leadership_election():

    global hardliner_committee
    global idealist_committee
    global moderate_committee

    player_votes = 0

    print("\nINTERNAL LEADERSHIP ELECTION")
    print("---------------------------")

    # Hardliners

    hardliner_score = hardliner_loyalty + random.randint(-10,10)

    if hardliner_vote:
        hardliner_score += 15

    if hardliner_score >= 50:

        print("The Hardliners endorse you.")

        player_votes += hardliner_committee

    else:

        print("The Hardliners back another candidate.")

    # Idealists

    idealist_score = idealist_loyalty + random.randint(-10,10)

    if human_candidate_vote:
        idealist_score += 10

    if idealist_score >= 50:

        print("The Idealists endorse you.")

        player_votes += idealist_committee

    else:

        print("The Idealists back another candidate.")

    # Moderates

    moderate_score = moderate_loyalty + random.randint(-10,10)

    if human_candidate_vote:
        moderate_score += 15

    if moderate_score >= 50:

        print("The Moderates endorse you.")

        player_votes += moderate_committee

    else:

        print("The Moderates back another candidate.")

    print()
    print("Committee votes won:", player_votes)

    if player_votes >= 51:

        print("You win the leadership election!")

    else:

        print("You lose the leadership election.")
leadership_election()