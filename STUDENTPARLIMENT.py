def pause(text):
    print(text)
    input()
def get_choice(valid_choices):
    while True:
        choice = input("Choice: ").upper()

        if choice in valid_choices:
            return choice

        print("Invalid choice.")
def show_stats():
    print("==========")
    print("CURRENT STATS")
    print("==========")
    print(f"Popularity: {popularity}")
    print(f"Influence: {influence}")
    print(f"Unity: {unity}")
    print(f"Organization: {organization}")
    print("==========")
    input("Press Enter...")
pause("You are a normal student in a large school")
pause("Earlier,this morning, the Prinicpal announced formation of a student council")
pause("Elections to the council will be held after a month")
print("will you run in the election?(Y/N)")
choice = get_choice(["Y", "N"])
if choice == "N":
    pause("You decide not to run in the election")
    pause("You continue life as a normal student")
    pause("Seriously, the game is a election simulator. Pick yes")
if choice == "Y": 
    pause("You decide to participate in the school politics")
    pause("There are Multiple Groups you may join to help and rise through the ranks")
    pause("1.Panther party")
    pause("Panther Party is a Centralized, Unified Party. It is full of established party figures. It is extremely efficient and has high popularity. Gaining influence is difficult.")
    pause("2.Goat Group")
    pause("Goat Group is a Chaotic, Unified party. It is based around the Goat. It has high popularity  but is inefficient. Gaining influence is not very easy.")
    pause("3.United Union")
    pause("United Union is a Decentralized, unfied Party. It is full of Clubs and committees around the school and is efficient. Gaining influence will be moderately easy.")
    pause("Chicken Coalition")
    pause("Chicken coalition is a extremely decentralized and Divided party. It is full of Independents and small factions. It has Moderate popularity but weak efficiency. Gaining influence is easy. Powerful if United. ")
    print("What will you choose")
    print("1.Panther Party")
    print("2.Goat Group")
    print("3.United Union")
    print("4.Chicken coalition")
    choice = get_choice(["1","2","3","4"])
    if choice == "1":
       pause("Panther Party, Hmm.")
       pause("An established Poltical Machine")
       pause("Popular,Organized,Efficent")
       pause("Also full of people waiting for a promotion")
       pause("Get comfortable.You might be a volunteer for a while")
       party_name = "Panther Party"
    if choice == "2":
        pause("Goat Group")
        pause("Looks like you also like DA GOAT")
        pause("I never understood the craze behind it")
        pause("The party isn't the most efficient")
        pause("Good Luck")
        party_name = "Goat Group"
    if choice == "3":
        pause("United Union")
        pause("A collection of clubs, committees, and organizations.")
        pause("Nobody agrees on everything.")
        pause("Nobody agrees on anything.")
        pause("In fact, they are currently debating the meeting agenda.")
        party_name = "United Union"
    if choice == "4":
        pause("Chicken Coalition.")
        pause("An alliance of independents and minor factions.")
        pause("Nobody is entirely sure who is in charge.")
        pause("Several members claim it is them.")
        pause("Good luck figuring that out.")
        party_name = "Chicken Coalition"
    pause(f"Now that you have joined {party_name}")
    pause("i will explain a few stats")
    pause("Influence - This is YOUR influence INSIDE the party.This DEFINES you position within the party")
    pause("Popularity - Your PARTY popularity. this directly decidesthe result of the election")
    pause("Unity - You party's Unity. Ability to co-ordinate and make decision. Directly impacts Popularity later in the game")
    pause("Organization - Your party's ability to campaign and execute decisions. Directly impacts Popularity Later in the game")
    pause("Good Luck")
    if party_name == "Panther Party":
        popularity = 70
        influence = 10
        unity = 85
        organization = 85
    if party_name == "Goat Group":
        popularity = 65
        influence = 10
        unity = 80
        organization = 40

    if party_name == "United Union":
        popularity = 55
        influence = 10
        unity = 75
        organization = 75

    if party_name == "Chicken Coalition":
        popularity = 50
        influence = 10
        unity = 35
        organization = 35
    pause("===== PARTY STATS =====")
    pause(f"Party: {party_name}")
    pause(f"Popularity: {popularity}")
    pause(f"Influence: {influence}")
    pause(f"Unity: {unity}")
    pause(f"Organization: {organization}")
    print("========")
    print("WEEK ONE")
    print("========")
    pause("All parties Kick of their election campaign")
    if party_name == "Panther Party":
      pause("The Panther Party is having a Rally")
      pause("You have two choices")
      print("A-Follow Party plan")
      print("B-Propose your own plan")
      print("What will you do?")
      choice = get_choice(["A", "B"])
      if choice == "A":
          pause("You decide to Follow the Party Startegy")
          pause("The Rally runs smoothly")
          popularity += 5
          organization += 3
          influence += 1
          unity += 5
      if choice == "B":
          pause("You decide to Propose your plan")
          pause("The Rally runs smoothly regardless")
          pause("but few senior members think you are causing division within the party")
          popularity += 3
          organization -= 3
          unity -= 5
          influence += 10
    if party_name == "Goat Group":
        pause("The Goat Group is organizing a rally")
        pause("You are assisting in the organization")
        pause("You have two ways to go about this rally")
        print("A- Organize a Serious Rally")
        print("B-Organize a Large Goat-themed rally")
        print("What will you do?")
        choice = get_choice(["A" , "B"])
        if choice == "A":
            pause("You organize a Serious rally")
            pause("Attendees are suprsies by the Porfessionalism")
            popularity += 3
            organization += 8
            influence += 3
            unity += 2
        if choice == "B":
            pause("You decide the Goat remains eternal")
            pause("The turnout is extremly high")
            pause("Teachers think the rally is a joke")
            popularity += 8
            organization -= 5
            unity += 2
            influence += 5
    if party_name == "United Union":
        pause("The United Union is organizing a rally")
        pause("You are asked to help organize it")
        pause("What will you do?")
        print("A-Organize most of it yourself")
        print("B-Organize it after consultation with the union")
        choice = get_choice(["A" , "B" ])
        if choice == "A":
            pause("You organize a Rally by yourself")
            pause("The rally goes smoothly because of efficient-decision making")
            pause("But a few committee heads and members feel upset because they were not consulted")
            popularity += 5
            influence += 8
            unity -= 4
            organization += 3
        if choice == "B":
            pause("You Consult each Major leader before organziing")
            pause("All leaders appreciate it")
            pause("But Attendees feel like there are too many leaders and too much beaurcracy")
            popularity += 5
            influence += 1
            unity += 4
            organization -= 3
    if party_name == "Chicken Coalition":
        pause("the chicken coalitions(s) begin their campaign(s)")
        pause("You have two ways to go about this")
        print("A-Organize your own rally")
        print("B-Attend and assist another Leader's Rally")
        choice = get_choice(["A" , "B"])
        if choice == "A":
           pause("You Organize your own rally with a few supporters")
           pause("Your influence rises")
           pause("However, The Students feel like there is extreme division among the Coalition")
           pause("Other leaders also become suspicious of you")
           popularity += 1
           organization += 0
           unity -= 5
           influence += 10
        if choice == "B":
            pause("You Attend another Leader's rally and help or organize it")
            pause("A few leaders See your commitment to a unfied message")
            pause("Students are also happy seeing a little more unity in the coalition")
            popularity += 4
            influence += 3
            unity += 5
            organization += 3
    show_stats()
    pause("The next day after the rallies")
    if party_name == "Panther Party":
        pause("You are asssigned to man the Offical Party booth")
        pause("You must answer the Questions of students")
        pause("What will you do?")
        print("A-Give offical party Answer")
        print("B-Give your Own answers")
        choice = get_choice(["A" , "B"])
        if choice == "A":
            pause("You stick to the offical answers")
            pause("A few students think you are a robot")
            pause("But the unfied message builds popularity")
            popularity += 6
            organization += 4
            unity += 3
            influence += 0
        if choice == "B":
            pause("You decide that Students will like practical answers more")
            pause("Students feel like you are grounded and do not make standard promiss")
            pause("Your influence and popularity among the party rises")
            pause("The Senior members see you with a suspicious look")
            popularity += 2
            organization += 1
            unity -= 5
            influence += 6
    if party_name == "Goat Group":
        pause("Teachers approach you")
        pause("They Demand that you stop the goat-Branded rallies in favour of more professional rallies")
        pause("Their reasoing being that this makes the elections a joke rather than actual student participation")
        pause("What will you do?")
        pause("A-Organize more professional campaigns")
        pause("B-Continue Goat-branded Campaigns")
        choice = get_choice(["A" , "B"])
        if choice == "A":
            pause("You Agree that the party could use some professionalism")
            pause("You help organize more Serious campaigns")
            pause("Some Goat Hardliners (Yes,they somehow exist) think you are abandoning Goat")
            popularity += 4 
            unity += 1
            influence +=2
            organization += 3
        if choice == "B":
            pause ("You deny the demand and say that Goat is non-negotiable")
            pause ("Some memebers applaude you for holding your stance")
            pause ("Others feel the party has become a joke")
            popularity += 7
            influence +=5
            unity +=1
            organization -= 5
    if party_name == "United Union":
        pause("You enter a Party meeting")
        pause("Several memebers are arguing")
        pause('"WE SHOULD FUND POSTERS!" ')
        pause('"NO! POSTERS WILL GET TORN DOWN BY ADMINSTRATION. WE NEED RALLIES!" ')
        pause('"FORGET RALLIES, WE SHOULD HAND OUT PIZZA AS A WELFARE PROGRAM" ')
        pause('Everyone:"What?" ')
        pause('Member:"it could work" ')
        pause("What will you do?")
        pause("A-Support one idea")
        pause("B-Try to reach a Comprimise")
        choice = get_choice(["A" , "B"])
        if choice == "A":
            pause("You Support the idea you think is best")
            pause("After a decision, a few members feel upset")
            organization += 5
            unity -= 5
            influence += 3
        if choice == "B":
            pause("You Help reach a Comprimise")
            pause("Several members applaud you for your committment to unity")
            pause("Others feel like the Union is becoming too in-efficient")
            organization -= 3
            unity += 5
            influence += 5 
    if party_name == "Chicken Coalition":
        pause("You attend a Coalition planning meeting")
        pause("Three faction leaders are arguing over campaign posters")
        pause('"My faction should be on the posters!"')
        pause('"No, MY faction has more support!"')
        pause('"Why are there even factions?"')
        pause("Nobody answers that question.")
        pause("What will you do?")
        pause("A-Support one faction")
        pause("B-Propose a joint campaign")
        choice = get_choice(["A", "B"])
        if choice == "A":
            pause("You publicly support one faction")
            pause("That faction is grateful for your support")
            pause("The others immediately become suspicious")
            influence += 6
            popularity += 2
            unity -= 5
            organization += 2
        if choice == "B":
            pause("You propose a joint campaign")
            pause("After a surprisingly civil discussion, the factions agree")
            pause("Nobody gets exactly what they wanted")
            pause("But everyone gets something")
            popularity += 3
            unity += 6
            organization += 4
            influence += 2
    show_stats()
    pause("You slowly start to get a say in decisions in the party.")
    pause("Your dedication is being noticed")
    if party_name == "Panther Party":
        pause("A Senior Panther Member recognizes your effort")
        pause("He offers to mentor you and help you become known")
        pause("In exchange, you join his network and help him build influence")
        pause("A-Accept")
        pause("B- Build your own support network")
        choice = get_choice(["A","B"])
        if choice == "A":
            pause("You accept his guidance")
            pause("You Gain experince and help organize his rallies")
            pause("However, you do not get much influence")
            pause("regardless, the part gains some unity")
            influence += 2
            unity += 4
            organization += 3
        if choice == "B":
            pause("You reject in favour of building on you network")
            pause("When others see you building your own influence, They feel like you are undermining the party")
            pause("Regradless, You gain influence at the cost of party unity and efficency")
            influence += 7
            unity -= 5
            organization -= 2 
    if party_name == "Goat Group":
        pause("The School newspaper editor wants to Interview the Party")
        pause("Some memebers want to send offical spokeperson")
        pause("While others feel like a goat mascot is the true represenation of the party")
        pause("You can support ethier side")
        pause("A-Support a Spokeperson")
        pause("B-Support a Mascot")
        choice = get_choice(["A","B"])
        if choice == "A":
            pause("You think that it's high time the party becomes more serious")
            pause("With you support, A spokeperson is sent")
            popularity += 5
            unity += 2
            organization += 5
            influence +=3
        if choice == "B":
            pause("You agree that only the goat can represent the party")
            pause("With your support, A mascot is sent")
            popularity += 7
            unity += 2
            organization -= 4
            influence += 4
    if party_name == "United Union":
        pause("A club threatens to leave the Union completely")
        pause("The Union is split on wether to give concessions or let them go")
        pause("What is your stance?")
        pause("A-Make concessions")
        pause("B-Let them go")
        choice = get_choice(["A","B"])
        if choice == "A":
            pause("You Recognize the need for the party to remain united at this time")
            pause("After negotiations, The club decides not to leave in exchange for concessions")
            popularity -= 2
            unity += 2
            organization -= 4
            influence += 3
        if choice == "B":
            pause("You decide that a single club is not worth making concession for")
            pause("Maybe it's better the disloyal leave early")
            popularity -= 3
            unity -= 4
            organization += 4
            influence += 5
    if party_name == "Chicken Coalition":
        pause("Two Coalition leaders are having a dispute")
        pause("Both scheduled rallies at the same location and time")
        pause("Neither leader is willing to change their plans")
        pause("The Coalition looks increasingly disorganized")
        pause("What will you do?")
        pause("A-Support one leader")
        pause("B-Try to negotiate a compromise")
        choice = get_choice(["A","B"])
        if choice == "A":
            pause("You publicly support one of the leaders")
            pause("The dispute is resolved quickly")
            pause("The other leader is not pleased")
            popularity -= 1
            unity -= 4
            organization += 4
            influence += 5
        if choice == "B":
            pause("You attempt to negotiate a compromise")
            pause("After a long discussion, the rallies are rescheduled")
            pause("Several leaders appreciate your effort")
            popularity += 2
            unity += 5
            organization -= 2
            influence += 3
    pause("All Parties Conclude thier campaigns for the week")
    pause("WEEK ONE COMPLETE")
    print("========")
    print("WEEK TWO")
    pause("========")
    def PP():
     return party_name == "Panther Party"
    def GG():
     return party_name == "Goat Group"
    def UU():
     return party_name == "United Union"
    def CC():
     return party_name == "Chicken Coalition"
    pause("After a week of campaigning, handling party matters, and other party stuff")
    pause(f"You recognize that {party_name} needs a Change")
    pause("You think the party needs a better leader")
    pause("Who do you think should be the leader")
    print("A-Competent senior memeber")
    print("B- You")
    choice = get_choice(["A", "B"])
    if choice == "A":
        pause("No, idiot.")
        pause("A competent senior member?")
        pause("Have you forgotten who the protagonist is?")
        pause("If you want to fix the party, Do it yourself")
    if choice == "B":
        pause("You?")
        pause("Bold.")
        pause("Questionable, but bold.")
        pause("I admire the confidence.")
        pause("Your campaign experience currently consists of existing.")
        pause("Well, at least somebody believes in you.")
    pause(f"Regardless, YOU need to lead {party_name}.")
    pause("The time has come to challenge the leadership.")
    if PP():
        support = 0
        pause("To Become the leader of the Panther Party, You must convince the Managing committee to election you as one during the upcoming leadership election")
        pause("There are three factions")
        pause("1.Traditionalist")
        pause("2.Reformers")
        pause("3.Organizers")
        pause("Convince at least 2 to become leader")
        pause("This will allow you to defeat the leadership and take command")
        pause("This will also allow you to become Student leader upon Panther Victory")
        pause("After the leadership elections are annoucned, you approach the traditionalists")
        pause('"Greetings" Says the Leader of the traditionalists')
        pause("Very Traditionalist")
        pause("They ask you to prevent reforms")
        pause("If you accept, you will not be able to get reform support")
        pause("Do you accept?(Y/N)")
        choice = get_choice(["Y","N"])
        if choice == "Y":
            pause('You:"Sure.I will not reform too much of the party"')
            pause('Traditional Leader: "EXCELLENT! we will vote for you in the upcoming vote. DO not betray us later')
            pause("Hopefully you do not betray")
            support += 1
            Traditional_support= True
            unity -= 4
        if choice == "N":
            pause('You:"No.The Party needs change" ')
            pause("The expression of his face turns dull")
            pause('Leader:"i thought we could work together." ')
            pause("They meetings ends with no support")
            support += 0
            Traditional_support = False
        pause("After meeting the traditionalist, You meet the Reformist")
        if Traditional_support:
            pause(' "It seems you have promised the tradistionalist Not to reform." ')
            pause('"We will not trust a two faced man" ')
            pause("Says the reformist leader")
            pause("The meeting ends without support")
        else:
            pause(' "We want reform" ')
            pause(' "Reform the party so it becomes easier for new members to have a voice." ')
            pause('"So members like you do not have to go out of way and try to beomce leader" ')
            pause("Ouch. that must have hurt. But he is saying the truth")
            pause("Do you accept though? (Y/N)")
            choice = get_choice(["Y", "N"])
            if choice == "Y":
                pause(' "Nice. we will get you the support" ')
                pause("Good work player. Do  not mess this up now")
                support += 1
                organization -= 3
                Reform_support = True
            if choice == "N":
                pause(' ""WOW. We were gonna help people like you." ')
                pause('"We wll find another person to support" ')
                Reform_support = False
                support += 0
                pause("Well that didnt go so well.")
        pause("Now we will meet the organizers")
        pause("hopefully, the Organizer's do not cause a issue")
        pause("Dont be late. they have organized the meeting")
        pause("When you go inside, there is only one person. They felt it was too in-efficient to send multiple")
        pause('"Let us be quick. Will you damage the organization of the party?"')
        pause('"Many ambitious members promise change."')
        pause('"Others promise tradition."')
        pause('"We do not care."')
        pause('"We care about results."')
        pause('"Will you give the Organizers greater authority over campaigns and party operations?"')
        pause("Do you accept? (Y/N)")
        choice = get_choice(["Y", "N"])
        if choice == "Y":
            pause('You:"Yes. The party needs efficient management."')
            pause('"Excellent."')
            pause('"Then you have our support."')
            pause("The Organizers agree to back your leadership campaign.")
            support += 1
            Organizer_support = True
            organization += 5
            influence -= 2
        if choice == "N":
            pause('You:"No. Too much power should not be concentrated in one group."')
            pause('"Unfortunate."')
            pause('"We prefer candidates who value efficiency."')
            pause("The meeting ends without an endorsement.")
            Organizer_support = False
        pause("The leadership vote is held.")
        pause(f"You secured support from {support} out of 3 factions.")
        if support >= 2:
            pause("The Managing Committee votes.")
            pause("After a tense count, you win the leadership election.")
            pause(f"You are now the Leader of the {party_name}.")
            party_position = "Party Leader"
            influence += 30
            leader = True
        else:
            pause("The Managing Committee votes.")
            pause("Your challenge falls short.")
            pause("However, many members are impressed by your campaign.")
            pause("You emerge as one of the most influential figures in the party.")
            party_position = "Major Figure"
            influence += 15
            leader = False
    if GG():
        pause("SPECIAL EVENT")
        pause("The Goat Group is thrown into chaos")
        pause("The School Administration has made a announcement")
        pause('"A Goat may not serve as the official leader of a political party."')
        pause("The party is stunned")
        pause("Several members begin arguing")
        pause('"This is tyranny!"')
        pause('"The Goat remains our true leader!"')
        pause('"We need an actual leader now!"')
        pause("Eventually, attention turns toward you")
        pause('"You should lead the party."')
        pause("The party agrees")
        pause("You are the leading candidate")
        if influence >= 60:
            pause("Your influence is already extremely high")
            pause("Most members support you immediately")
            pause("You become the official leader of the Goat Group")
            party_position = "Party Leader"
            leader = True
            influence += 30
        else:
            pause("Some members are unsure")
            pause("You must decide how to secure support")
            print("A-Promise to preserve the Goat Tradition")
            print("B-Promise a more professional future")
            choice = get_choice(["A","B"])
            if choice == "A":
                pause("You promise that the Goat will remain the soul of the party")
                pause("Members cheer")
                pause("The Goat remains eternal")
                popularity += 5
                unity += 5
                influence += 20
                party_position = "Party Leader"
                leader = True
            if choice == "B":
                pause("You promise to modernize the party")
                pause("Some members are disappointed")
                pause("Others are impressed")
                organization += 8
                popularity += 2
                influence += 20
                party_position = "Party Leader"
                leader = True
        pause("The Goat is officially replaced as party leader")
        pause("The Goat remains Party Mascot")
        pause("This is considered a acceptable compromise")
    if UU():

        pause("SPECIAL EVENT")

        pause("The United Union has grown rapidly")

        pause("Several leaders complain that decision-making has become slow")

        pause("Others argue that every club deserves a voice")

        pause("A historic proposal is introduced")

        pause('"The Centralization Act"')

        pause("The Act would give the Union Leadership greater authority")

        pause("Many members support it")

        pause("Many members oppose it")

        pause("The future of the Union is uncertain")

        pause("As one of the Union's leading figures, your position is critical")

        print("A-Support the Centralization Act")

        print("B-Oppose the Centralization Act")

        choice = get_choice(["A","B"])

        if choice == "A":

            pause("You support the Act")

            pause("After intense debate, the proposal passes")

            pause("The Union becomes significantly more centralized")

            pause("Decision-making becomes faster")

            pause("Some clubs complain about losing influence")

            organization += 12

            unity -= 4

            influence += 10

            popularity += 3

            party_position = "Central Union Leader"

        if choice == "B":

            pause("You oppose the Act")

            pause("After intense debate, the proposal fails")

            pause("The Union remains decentralized")

            pause("Many clubs celebrate the decision")

            pause("Others worry that the Union will remain inefficient")

            unity += 8

            organization -= 4

            influence += 10

            popularity += 2

            party_position = "Union Defender"
    if CC():

        pause("SPECIAL EVENT")

        pause("The Chicken Coalition remains the smallest political force in the school")

        pause("Several leaders privately admit that the Coalition cannot win in its current form")

        pause("Too many groups")

        pause("Too many leaders")

        pause("Too many disagreements")

        pause("A historic summit is called")

        pause("All Coalition leaders gather to discuss the future")

        pause("You present a proposal")

        pause('"The Chicken Union"')

        pause("A single organization")

        pause("A single campaign")

        pause("A single message")

        pause("The room falls silent")

        if influence >= 20:

            pause("Your influence gives the proposal immediate credibility")

            pause("Several leaders endorse the plan")

            pause("After negotiations, the proposal passes")

            pause("The Chicken Union is born")

            popularity += 10

            unity += 15

            organization += 10

            influence += 10

            party_position = "Founder of the Chicken Union"

        else:

            pause("Many leaders are skeptical")

            pause('"Why should we follow you?"')

            pause("You must convince them")

            print("A-Promise positions to coalition leaders")

            print("B-Promise a stronger election campaign")

            choice = get_choice(["A","B"])

            if choice == "A":

                pause("Several leaders are offered positions in the future Union")

                pause("Most agree to join")

                pause("The Chicken Union is established")

                popularity += 5

                unity += 12

                organization += 8

                influence += 5

                party_position = "Founder of the Chicken Union"

            if choice == "B":

                pause("You argue that unity is the only path to victory")

                pause("The speech is surprisingly effective")

                pause("After lengthy debate, the proposal passes")

                popularity += 8

                unity += 10

                organization += 6

                influence += 8

                party_position = "Founder of the Chicken Union"