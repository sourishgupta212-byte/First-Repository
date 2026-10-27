def get_choice(prompt, valid_choices):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a number.")


print("=== Holiday Calculator ===")
print("This calculator estimates the probability of a school holiday.\n")

# Weather
choice = get_choice(
    "\nWeather Forecast:\n"
    "1. Sunny\n"
    "2. Cloudy\n"
    "3. Light rain\n"
    "4. Heavy rain\n"
    "5. Foggy\n"
    "Choice: ",
    [1, 2, 3, 4, 5]
)

if choice == 1:
    W = 0
elif choice == 2:
    W = 10
elif choice == 3:
    W = 20
elif choice == 4:
    W = 45
else:
    W = 40
# Events
choice = get_choice(
    "\nEvent Factor:\n"
    "1. No event\n"
    "2. Local event\n"
    "3. Big event\n"
    "4. Major event\n"
    "5. Large unexpected event\n"
    "Choice: ",
    [1, 2, 3, 4, 5]
)
if choice == 1:
    E = 0
elif choice == 2:
    E = 5
elif choice == 3:
    E = 10
elif choice == 4:
    E = 20
else:
    E = 30
# Disruptions
choice = get_choice(
    "\nDisruption Factor:\n"
    "1. No disruption\n"
    "2. Minor transport disruption\n"
    "3. Major disruption\n"
    "4. Total blockade\n"
    "Choice: ",
    [1, 2, 3, 4]
)

if choice == 1:
    D = 0
elif choice == 2:
    D = 10
elif choice == 3:
    D = 25
else:
    D = 50

# Communication
choice = get_choice(
    "\nCommunication Factor:\n"
    "1. No news\n"
    "2. Minor news\n"
    "3. Major news\n"
    "4. Major school rumor\n"
    "5. Teacher-supported rumor\n"
    "Choice: ",
    [1, 2, 3, 4, 5]
)

if choice == 1:
    C = 0
elif choice == 2:
    C = 10
elif choice == 3:
    C = 15
elif choice == 4:
    C = 20
else:
    C = 25

# Day of Week
choice = get_choice(
    "\nDay of Week:\n"
    "1. Monday\n"
    "2. Tuesday\n"
    "3. Wednesday\n"
    "4. Thursday\n"
    "5. Friday\n"
    "6. Saturday\n"
    "Choice: ",
    [1, 2, 3, 4, 5, 6]
)

if choice == 1:
    DOW = 0
elif choice == 2:
    DOW = 1
elif choice == 3:
    DOW = 2
elif choice == 4:
    DOW = 4
elif choice == 5:
    DOW = 8
else:
    DOW = 15

# Final Calculation
score = W + E + D + C + DOW
probability = score / 165 * 100

print("\n=== Results ===")
print(f"Score: {score}/165")
print(f"Holiday Probability: {probability:.2f}%")

if probability < 25:
    print("Verdict: Pack your bag. 😭")
elif probability < 50:
    print("Verdict: Possible, but don't get your hopes up. 😐")
elif probability < 75:
    print("Verdict: Decent chance. 😎")
else:
    print("Verdict: The calculator is feeling optimistic. 🎉")
print("\nFactor Breakdown:")
print(f"Weather: {W}")
print(f"Events: {E}")
print(f"Disruption: {D}")
print(f"Communication: {C}")
print(f"Day of Week: {DOW}")
input("\nPress Enter to exit.")