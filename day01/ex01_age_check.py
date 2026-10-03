# Exercise 1 — START FROM A BLANK FILE (write your solution below)
#
# Requirement:
# Ask the user for their age.
# If they are 18 or older, print: Adult
# Otherwise, print: Minor

def check_age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
    return age


check_age()