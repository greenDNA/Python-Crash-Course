vacation = {}
poll_active = True
number = 1
user = None
while poll_active:
    print("If you can visit one place in the world, where?")
    user = input("> ")
    vacation[str(number)] = user
    number += 1
    print(vacation)
    if user == 'q':
        poll_active = False
print("Exiting")
