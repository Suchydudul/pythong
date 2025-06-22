Intial_pricipal_balance = 0
Interest_rate = 0 
times = 0

while Intial_pricipal_balance <= 0:
    Intial_pricipal_balance = float(input("Please neter the principle amount "))
    if Intial_pricipal_balance <=0:
        print("principle cannot be equal or less than zero ")

while Interest_rate <= 0:
    Interest_rate = float(input("Please enter the inbterest rate "))
    if Interest_rate <= 0:
        print("interest rate cannot be less or equal to zero ")


while times <= 0:
    times = int(input("Please enter the time in years  "))
    if times <= 0:
        print(" Years cannot be less or equal to zero ")


final_amount = Intial_pricipal_balance * pow((1 + Interest_rate/100), times)

print(f"The final amount after {times} year/s will be ${final_amount:.2f}")