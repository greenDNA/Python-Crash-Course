def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for index in range(0, len(magicians)):
        magicians[index] += ' the Great'
    return magicians
magicians = ['abra', 'kadabra', 'alakazam']
magicians2 = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians2)
