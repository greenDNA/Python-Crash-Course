import json

print("Enter your favorite number")
number = input("> ")
with open('number.txt', 'w') as objectfile:
    json.dump(number, objectfile)
#with open('number.txt') as objectfile:
#    number = json.load(objectfile)
#    print(number)
