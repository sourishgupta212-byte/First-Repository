print("Please enter your marks")
english = int(input("English: "))
maths = int(input("Maths: "))
science =int(input("Science: "))
hindi = int(input("Hindi: "))
punjabi = int(input("Punjabi: "))
Computer = int(input("IT: "))
Social = int(input("SST: "))
total = english + maths + science + hindi + punjabi + Computer + Social
total_percentage = total / 560
percentage = total_percentage*100
print("Percentage" , round(percentage, 2),"%")
input()
if percentage >= 90:
    print("TOP STUDENT")
elif percentage >= 80:
    print ("Very good")
elif percentage >= 70:
    print("Good")
elif percentage >= 60:
    print("Need improvement")
elif percentage >= 50:
    print("Bad")
elif percentage >= 40:
    print("VERY bad")
elif percentage >= 33:
    print("BARELY PASSED")
else:
    print("You failed.")
input()

