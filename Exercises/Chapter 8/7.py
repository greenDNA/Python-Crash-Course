def make_album(name, title, tracks=''):
    return {name : title, 'tracks' : tracks}

album1 = make_album(name='Sabrina Claudio', title='About Time')
album2 = make_album('6lack', 'Free 6lack', 13)
album3 = make_album('Miguel', 'Kaleidescope Dream')
print(album1)
print(album2)
print(album3)
