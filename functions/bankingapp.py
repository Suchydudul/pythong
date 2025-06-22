def show_balance(balance):
    print(f"Your current balance is {balance}$\n")
    pass

def withdraw(balance):
    withdraw_amount = input("Please provide the amount to withdraw: ")
    if withdraw_amount.isdigit() == False:
            print(f" {withdraw_amount} is not a number\n")
            return balance
    withdraw_amount = int(withdraw_amount)
    if withdraw_amount > balance:
        print("Not enough balance\n")
    else: 
        print(f"You withdrawn {withdraw_amount}$ \n")
        new_balance = balance - withdraw_amount
        return new_balance


def deposit(balance):
    deposit_amount = input("Please provide the amount to deposit: ")
    if deposit_amount.isdigit() == False:
            print(f" {deposit_amount} is not a number\n")
            return balance
    deposit_amount = int(deposit_amount)
    print(f"You deposit {deposit_amount}$ \n")
    new_balance = balance + deposit_amount
    return new_balance


def main():
    balance = 1000
    print("welcome to the integer bank, not everythign floats our boats") # i hate myself for this
    while True:
        
        print("Select operation:")
        print("1. Show Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("Q. Quit\n" )
        selection = input()
        match selection.upper():
            case "1":
                show_balance(balance)
            case "2":
                balance = withdraw(balance)
                
            case "3":
                balance = deposit(balance)
            case "Q":
                print("Goodbye")
                break
            case _:
                print("invalid Operation\n")

if __name__ == "__main__":
    main()