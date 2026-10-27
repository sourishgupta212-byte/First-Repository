def pause(text):
    print(text)
    input()
def choose(valid_choices):
    while True:
     Choice = input("Enter your choice: ").upper()
     if Choice in valid_choices:
         return choice
     else:
         print("invalid Choice") 
violations = 0
files_processed = 0
files_approved = 0
files_rejected = 0
accuracy = 0 
def Accuracy():
     accuracy = ((files_processed - violations) / files_processed)*100
     return accuracy
pause("Three months ago, You applied for a job at the Ministry of approvals, In department of Approval for Public works")
pause("After a interview after a month of applying, they said a letter will be sent to you in week appointing or rejection you")
pause("Two months later, A letter arrived")
pause("""
                         GOVERNMENT OF THE REPUBLIC
                     Ministry of Administrative Affairs

Ref. No. MAA/HR/2047/017
Date: 17 October 2047

OFFICIAL APPOINTMENT LETTER
To,
The Appointed Officer
Subject: Appointment to the Office of Junior Approval Officer
Sir/Madam,
Following a review of your application, educational qualifications, and apparent willingness to accept responsibility, the Government is pleased to appoint you to the post of Junior Approval Officer, Ministry of Administrative Affairs, with effect from the date of your reporting.
Your principal duties shall include:
1. Examining applications submitted by citizens.
2. Approving or rejecting requests in accordance with applicable regulations.
3. Maintaining accurate records of all decisions.
4. Referring matters of exceptional complexity to the Director, including matters that could reasonably have been resolved without referral.

You shall be provided with one desk, one official stamp, and access to the Ministry's application register, subject to availability.

Please note that the acceptance of this appointment does not automatically entitle the appointee to a functioning desk drawer.

You are directed to report to the Department of General Approvals at 09:00 hours on the next working day.

We trust that you will discharge your duties with diligence, impartiality, and an appropriate degree of concern regarding Form 27-B.

Yours faithfully,
Secretary to the Government
Ministry of Administrative Affairs
By order of the Director of Personnel
""")
pause("Congratulations! You have been appointed!")
pause("You Arrive the next day")
pause("You find your desk and sit down")
print("""
A - Ponder how far you have come
B - Begin work immidiately
""")
choice = input("Your Choice: ")
if choice == "A":
    pause("You think about how far you have come")
    pause("then you relaize you really haven't.")
    pause("You are just a Junior officer")
    pause("You decide to get to work")
else:
    print("You decide to get to work immdiately")
pause("You see your desk")
pause("There is a large amount of folders, and a computer")
pause("And a suprisngly small number of staplers")
pause("You boot up the computer")
pause("There you see the ministry uses it's own app for proccessing")
pause("""
MINISTRY OF ADMINISTRATIVE AFFAIRS — INTERNAL SYSTEM
GENERAL APPROVALS TERMINAL
Officer: Junior Approval Officer
Pending applications: 3
System status: Operational*

*Operational does not guarantee functionality.""")
pause('"Concering" you say')
pause("You see the folder on the top")
pause("APPLICATION: 0893")
pause("You open it")
pause("""
GENERAL APPROVALS TERMINAL
FILE 0893


DEPARTMENT OF PUBLIC WORKS
REQUEST FOR STREETLAMP REPAIR
Applicant: Municipal Councillor, Ward 14
Request: Repair one streetlamp outside the Ward 14 public library.
Estimated cost: ₹2,400
Reason: The streetlamp has been non-functional for eleven days, making the road difficult to use after sunset.
Documents submitted:
- Repair request form
- Cost estimate from the municipal electrician
- Photograph of the damaged streetlamp

OFFICER'S NOTE
The request form lists the location as Ward 14, Library Road.
However, the electrician's estimate lists the location as Ward 14, Old Library Road.
Both documents bear the correct municipal seal.
No other discrepancies detected.
 """)
print("""
A - Approve file
B - Reject file
C - Return for corection 
 """)
choose(["A","B","C"])
if choice == "A":
    pause("You approve the file")
    pause('"What could possibly go wrong?" You say')
    pause("Honestly, a Lot")
    files_processed += 1
    files_approved += 1
