name = input("enter your name: ")
lenght = len(name)
alphacheck= name.isalpha()
spacescheck = name.find("-")

if(lenght <= 12 and alphacheck == True and spacescheck == -1):
    print(f"Your username is {name}, your user name is valid")
else:
    print(f"Your username is {name}, your user name is invalid")
