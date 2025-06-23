import random
import time
def play(bet):
    session = ["","",""]
    for x in range(0,3):
        session[x]=(random.choice(["1","2","3"]))
        time.sleep(0.2)
        print(f"{session[x]} ", end="", flush=True)
    print("")
    if session[0] == session[1] == session[2]:
        match session[0]:
            case "1":
                return bet*2
            case "2":
                return bet*5
            case "3":
                return bet*10
    else: 
        return 0-bet

def main():

    money = 100
    bet = 5

    while True:
        print("*********************************************************")
        print(f"Welcome to the slot machines, your current money is {money}$")
        print("*********************************************************")
        print(f"Current bet is: {bet}")
        print("Your options are:")
        print("1.) Play")
        print("2.) Increase bet")
        print("3.) Decrease bet")
        print("4.) Quit")   
        selection=input("")
        match selection:
            case "1":
                money += play(bet)
            case "2":
                bet=bet+5
            case "3":
                if bet == 5:
                    print("Bet cant be lower than 5$")
                else:
                    bet=bet-5
            case "4":
                print("Thanks for playing")
                break
        
        

        
if __name__ == "__main__":
    main()