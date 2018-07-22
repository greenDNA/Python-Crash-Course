with open('buster.txt') as objectfile:
    count = 0
    for line in objectfile:
        count += line.count('the')
    print(count)
