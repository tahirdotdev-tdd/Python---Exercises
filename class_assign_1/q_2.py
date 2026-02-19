"""
 Write a program that prints the numbers from 1 to 10 on a single line, separated
by a comma and a $ character.

Solution⬇️: 

"""
for i in range(1,11):
    if i < 10: 
        print(i, end=",$")
    else:
        print(i)
