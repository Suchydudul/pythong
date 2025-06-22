menu = {
    "dum":5,
    "mint":3,
    "diss":2
      }

cart = []
total = 0 
print("-------menu-------")
for key, value in menu.items():
    print(f"{key}: {value}")
print("------------------")
while True:
    stuff = input("Select an item from teh menu (q to quit): ").lower()
    if stuff == "q":
        break
    elif menu.get(stuff)is not None:
        cart.append(stuff)
        total += menu.get

print (cart)
print (total)        

