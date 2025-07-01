try:
    number = int(input("Please provide a number: "))
    print (1 / number)
except ZeroDivisionError:
    print(" You cannot divide by 0 ")
except ValueError:
    print("enter only numbers")
finally:
    print("cleanup should be here")