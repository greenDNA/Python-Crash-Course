sandwich_orders = ['pastrami', 'supreme', 'pastrami', 'meat', 'veggie', 'pastrami']
finished_sandwiches = []
print("We have run out of pastram!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print("I made you your {} sandwich!".format(sandwich))
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
