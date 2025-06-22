def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z    

def multiply(x, y):
    z = x * y
    return z    

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    z = x / y
    return z

def power(x, y):
    z = x ** y
    return z

def __main__():
    print("Please provide 2 numbers")
    x = input(" x = ")
    y = input(" y = ")
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    module = input("Please select a module (add, subtract, multiply, divide, power): ").lower()
    if module == "add":
        result = add(x, y)  
    elif module == "subtract":
        result = subtract(x, y) 
    elif module == "multiply":  
        result = multiply(x, y)
    elif module == "divide":
        result = divide(x, y)
    elif module == "power":
        result = power(x, y)
    else:
        print("Invalid module selected.")
        return
    print(f"The result of {module}ing {x} and {y} is: {result}")

if __name__ == "__main__":
    __main__()
