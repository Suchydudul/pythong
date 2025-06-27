import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "

chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"key {key}")
encrypted_user_input = ""
user_input = input("Please write your message to encrypt: ")
for letter in user_input:
    index = chars.index(letter)
    encrypted_user_input += key[index]

print(encrypted_user_input)
