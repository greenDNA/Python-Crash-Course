def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for index in range(0, len(magicians)):
        magicians[index] += ' the Great'
magicians = ['abra', 'kadabra', 'alakazam']
make_great(magicians)
show_magicians(magicians)
