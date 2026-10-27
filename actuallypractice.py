def get_choice(valid_choices):
 while True:
  choice = input("Enter your choice: ").upper()
  if choice in valid_choices:
   return choice
  else:
   print("Invalid choice")
def approve(record, item, key, change):
  record[item][key] = change
applications = [{"Name" : "Road Repair","Status" : "Pending",},
 {"Name" : "Pipe repair","Status" : "Pending"}]
for item  in applications:
 name = item["Name"]
 status = item["Status"]
 print(f"{name} - {status}")
print("""
A - Approve A
B - Approve B
C - Approve both
D - Remain pending
E - Reject A
F - Reject B
G -  Reject both 
""")
choice = get_choice(["A", "B", "C", "D", "E", "F", "G"])
if choice == "A":
 print("A approved")
 approve(applications,0,"Status", "Approved")
if choice == "B":
 print("B Approved")
 approve(applications,1,"Status", "Approved")
if choice == "C":
  approve(applications,0,"Status", "Approved")
  approve(applications,1,"Status", "Approved")
  print("Very generous of you")
if choice == "D":
 print("Do your job at least...")
if choice == "E":
 print("A Rejected")
 approve(applications,0,"Status", "Rejected")
if choice == "F":
 print("B Rejected")
 approve(applications,1,"Status", "Rejected")
if choice == "G":
  approve(applications,0,"Status", "Rejected")
  approve(applications,1,"Status", "Rejected")
  print("Nobody likes you")
for item  in applications:
 name = item["Name"]
 status = item["Status"]
 print(f"{name} - {status}")
