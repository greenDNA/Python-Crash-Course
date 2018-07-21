age = None
while True:
    print("What is your age?")
    age = int(input("> "))
    if age < 3:
        print("Free!")
    elif age >= 3 and age < 12:
        print("$10!")
    else:
        print("$15!")
#Ctrl-C to quit
