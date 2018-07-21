cubes = [cube**3 for cube in range(1, 11)]
for cube in cubes:
    print(cube)
print("First three items: {}".format(cubes[:3]))
print("Three from the middle: {}".format(cubes[int(len(cubes)/2):int(len(cubes)/2)+3]))
print("Last three: {}".format(cubes[len(cubes)-3:]))
