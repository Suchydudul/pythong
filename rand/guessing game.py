import random

number = random.randint(0,100)

while True:
    guess = int(input("Guess a number form 0 to 100 \n " ))
    if guess == number:
        print ("You guessed the number!")
        break
    elif guess < number:
        print (f"The number you are looking for is higher than: {guess}")
    elif guess > number:
        print (f"The number you are looking for is lower than: {guess}")
