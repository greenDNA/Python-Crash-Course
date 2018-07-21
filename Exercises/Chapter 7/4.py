toppings = []
choice = None
while True:
    print("What would you like to add to your pizza?")
    choice = input("> ")
    if choice == 'q':
        break
    toppings.append(choice)
    print(toppings)
print("Exiting")
