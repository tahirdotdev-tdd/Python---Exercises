# Get user input
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Perform calculations and handle division by zero
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "Error"
mod = num1 % num2 if num2 != 0 else "Error"
f_div = num1 // num2 if num2 != 0 else "Error"

# Create a simple manual table using f-strings for alignment
print("\n+----------------+----------+")
print(f"| {'Operation':<14} | {'Result':<8} |")
print("+----------------+----------+")
print(f"| {'Addition':<14} | {add:<8} |")
print(f"| {'Subtraction':<14} | {sub:<8} |")
print(f"| {'Multiplication':<14} | {mul:<8} |")
print(f"| {'Division':<14} | {div:<8} |")
print(f"| {'Modulus':<14} | {mod:<8} |")
print(f"| {'Floor Div':<14} | {f_div:<8} |")
print("+----------------+----------+")