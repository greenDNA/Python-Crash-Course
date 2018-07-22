import json

def greet_user():
    with open('remember.txt') as objectfile:
        name = json.load(objectfile)
    return name

def get_new_username():
    with open('remember.txt', 'w') as objectfile:
        print("What is your name?")
        name = input("> ")
        json.dump(name, objectfile)

print("Are you {}? (y/n)".format(greet_user()))
if input().lower() == 'y':
    print("Welcome back {}".format(greet_user()))
else:
    get_new_username()
