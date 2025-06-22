import math
operator =  input("Enter and operator (+,-,/,*) ")
a = int(input("Enter a "))
b = int(input("Enter b "))

if operator == "+":
    result = a + b
    print(f"result = {result}")

elif operator == "-":
    result = a - b
    print(f"result = {result}")

elif operator == "*":
    result = a * b
    print(f"result = {result}")

elif operator == "/":
    result = a / b
    print(f"result = {result}")

else:
    print("Invalid operator")

