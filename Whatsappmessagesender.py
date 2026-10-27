import pywhatkit as kit

# Replace with your friend's phone number (include country code, e.g., +91 for India)
phone_number = "+91 98786 78350"  
message = "Hey! Just a random 2 AM check-in. hope you're asleep!"

print("Scheduling message for 8:37 PM...")

# kit.sendwhatmsg(phone_number, message, hour_in_24_format, minute)
kit.sendwhatmsg(phone_number, message, 20, 40)

print("Message scheduled successfully. Keep your computer awake!")

