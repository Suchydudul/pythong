#guessing game
secret_word = "123"



while True:

    letter = input("try guessing the secret word (you can try a letter or a sequnce): ")
    if letter.lower() == secret_word.lower():
        print(f"You guessed the word: {secret_word}")
        break
    if letter.lower() in secret_word.lower():
        print(f"{letter} is in the word")
    else:
        print(f"{letter} is not in the word")

