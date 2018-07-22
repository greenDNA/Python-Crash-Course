with open('guest_book.txt', 'w') as objectfile:
    while True:
        name = input("What is your name?\n> ") + "\n"
        print("Hello {}, your visit has been recorded.".format(name.strip()))
        objectfile.write(name)
