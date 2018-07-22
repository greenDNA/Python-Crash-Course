import json

print("Enter your favorite number")
number = input("> ")
with open('number.txt', 'w') as objectfile:
    json.dump(number, objectfile)
    print("Saving")

print(number)
print("Resetting number to 0")
number = 0

with open('number.txt') as objectfile:
    number = json.load(objectfile)
    print("Loading")
    print(number)
