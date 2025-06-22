shopping_cart = []
print("Welcome to the cum shoppin center, ")
while True:
    shopping_cart.append(input("Please let us know wha would you like to buy (type q to quit): "))
    if shopping_cart[len(shopping_cart) -1] == "q":
        shopping_cart.remove("q")
        break
print(f"Thanks for visiting, your shooping list is as follows {shopping_cart}")
