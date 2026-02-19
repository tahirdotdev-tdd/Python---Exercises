

"""
Prompt the user to enter their first and last name. Store them in two separate
variables and print them in reverse order (last name first), separated by a com

Solution⬇️: 

"""

fName = input("Enter your first name: ")
lName = input("Enter your last name: ")

names = [fName, lName]

for s in reversed(names):
    print (s, end=', ')
