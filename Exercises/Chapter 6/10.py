numbers = {
    'sam' : [3],
    'mike' : [5, 9],
    'donald' : [6],
    'val' : [0],
    'sue' : [2, 3, 8]
}
for value, key in numbers.items():
    print("{} ".format(value))
    for elements in key:
        print("{}".format(elements))
