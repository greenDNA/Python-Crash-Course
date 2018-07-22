with open('likes.txt', 'w') as objectfile:
    while True:
        objectfile.write(input("Why do you like to program?\n> ") + "\n")
