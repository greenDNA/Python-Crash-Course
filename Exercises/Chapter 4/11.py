pizza = ['supreme', 'meat', 'pineapple']
for choice in pizza:
    print(choice)
    print("Nothing else compares to {}".format(choice))
print("I really, really like pizza")
friend_pizzas = pizza[:]
pizza.append("veggie")
friend_pizzas.append("bacon")
print(pizza)
print(friend_pizzas)
