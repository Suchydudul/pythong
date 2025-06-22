numbers = (1,2,3,4,5) # tuple
fruits = {"apple", "banana", "orange"} #set
dictionary = {"A":1,             #dictionary
              "B":2,
              "C":3}
string_name= "Dawid"

for number in numbers:
    print(number, end = "-")

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print(f"{key} :  {value}")