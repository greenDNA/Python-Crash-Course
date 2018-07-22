try:
    with open('cats.txt') as objectfile:
        for line in objectfile:
            print(line)
    with open('dogss.txt.') as objectfile:
        for line in objectfile:
            print(line)
except FileNotFoundError:
    print("File does not exist")
