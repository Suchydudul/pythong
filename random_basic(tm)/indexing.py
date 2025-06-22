#creditcard_number = "1235-4243-5453-2344"
#print(creditcard_number[]) 
#print(creditcard_number[::-1])

number = input("please provide your credit card number: ") 
number = number.replace("-","")
while not (number.isdigit and len(number) == 16):
    
    print("Your number is invalid, check the format (xxxx-xxxx-xxxx-xxxx)")
    number = input("please provide your credit card number: ") 
    number = number.replace("-","")
print(f"Your last 4 digits are: {number[-4:]}")

