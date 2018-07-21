names = ['nicki minaj', 'sabrina claudio', '6lack']

print('{} you are invited.\n{} you are invited.\n{} you are invited.'.format(names[0], names[1], names[2]))
print("{} can't make it".format(names[0]))
names[0] = 'akon'
print('{} you are invited.\n{} you are invited.\n{} you are invited.'.format(names[0], names[1], names[2]))
print("sia, adele, and pink will be joining the dinner.")
names.insert(0, 'sia')
names.insert(int(len(names)/2), 'adele')
names.append('pink')
print(names)
