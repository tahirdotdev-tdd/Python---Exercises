"""
Write a Python computer program that:
• Prints your name and student id on screen showing output as:
My name is “your name”✅
My student id is “your student id”.✅
• Prints the above two strings in a single line separated with!!✅
• Assigns the string “Welcome to the University" to a variable, greet.✅
• Assign the string “good” to a variable, feel.
• Prints the above two strings with a single print() function using the
variable names and concatenation showing output as:
Greetings: Welcome to the University!
I am glad that you feel good!✅
• Prints the string “Happy!" with a single print() function using the
variable mood.✅

"""
greet = "Welcome to the University"
feel = "Good"

name = input("What is your name?",)
id = input("What is your student id?")
_name = "My name is " + name 
_id = "My student id is " + id
print(_name, end="!!")
print(_id)

print("Greetings: " + greet + "! I am glad that you feel " + feel + "!")
mood = "Happy" + "!"
print(mood)

