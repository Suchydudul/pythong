import random
import os 
os.system("")
opponent = random.choice(["rock","paper","scissors"])
player = input("Please select your move: (Rock, Paper or scissors) ").lower()
print(f"Player selected: {player}\nOpponent selected: {opponent} \n")

match player:
    case x if player == opponent:
        print("\x1b[0;34m Its a tie! \n \x1b[39;49m")
    case "rock":
        if opponent == "scissors":
            print("\x1b[0;32m You won! \n \x1b[39;49m")
        else: 
            print("\x1b[0;31m You lost! \n \x1b[39;49m")
    case "paper":
        if opponent == "rock":
            print("\x1b[0;32m You won! \n \x1b[39;49m")
        else: 
            print("\x1b[0;31m You lost! \n \x1b[39;49m")
    case "scissors":
        if opponent == "paper":
            print("\x1b[0;32m You won! \n \x1b[39;49m")
        else: 
            print("\x1b[0;31m You lost! \n \x1b[39;49m")
    case _:
        print("\x1b[0;31m Inavalid input, You lost! \n \x1b[39;49m")

