def pause(text):
    print(text)
    input()
pause("The Election results are in")
pause("No one has a majoirty")
pause("""
===============
ELECTION RESULT
===============
National Democratic Party : 76/200
Labour Party: 70/200
Agranian Socialist Union : 25/200
Liberal party: 27/200
Independents : 2/200
""")
democratic = 76
labour = 70
agranian  = 25
liberal = 27
ind = 2
democratic_position = 6
labour_position = 3
agranian_position = 2
liberal_position = 5
ind_position = 4
government_formed = False
Coalitons = [""]
print("Possible coalitions")
left_seats = labour + agranian
reform_seats = democratic + liberal 
grand_left_seats = agranian + labour + ind
if labour + agranian  >= 100:
    pause(f"Left coalition : Labour + Agranian: {left_seats} seats ")
    Coalitons.append("Left Coalition")
if democratic + liberal >= 100:
    pause(f"Reform Coalition : Democratic + Liberal: {reform_seats} seats ")
    Coalitons.append("Reform Coaliton")
if grand_left_seats > 100:
    pause(f"Grand left coalition: Labour + Agranian + Independents : {grand_left_seats} seats")
    Coalitons.append("Grand Left Coalition")
def choose(valid_choices):
     while True:
      choice = input("Enter the Coaltion name you wish to form: ").lower
      if choice in valid_choices:
          return choice
governing_coalition = ""
choice = choose(Coalitons)
if choice == "left coalition":
    government_formed = True
    labour_status = "Coalition"
    governing_coalition = "Left coaliton"
if government_formed == False:
     democratic_farmer_seats = democratic +  agranian
     grand_right_seats = democratic + ind + liberal
     left_liberal_seats = liberal + labour
     pause("No natural Coalition is possible")
     pause("Parties are attempting to form desperate coalitions ")
     print("NEW POSSIBLE COALTIONS ")
     if agranian_position - democratic_position <= abs(2) and agranian + democratic >= 101:
         pause(f"Democratic agranian coalition: Democratic + Agranian : {democratic_farmer_seats} seats")
         Coalitons.append("Democratic Agranian coalitions")
     if grand_right_seats > 100:
         pause(f"Grant right coalition: Democratic + Liberal + Independents : {grand_right_seats} seats")
         Coalitons.append("Grand Right coalitions")
     if left_liberal_seats >100:
         pause(f"Left-Liberal coalition: Labour + Liberal : {left_liberal_seats} seats")
         Coalitons.append("Left-liberal Coalition")
if government_formed == False:
     pause("...")
     pause("MAYBE let's add independents to every coaliton and see")
     if left_seats + ind > 101:
        pause("left + Independents is possible")
        Coalitons.append("Left + Independents")
     if left_liberal_seats + ind > 101:
        pause("left liberal + Independents is aslo possible")
        Coalitons.append("Left Liberal + Independents")
     if labour + agranian + ind + liberal > 100:
        pause("A Grand Left + Liberal is possible")
        Coalitons.append("Grand left + Liberal")
     pause([Coalitons])