def make_album(name, title, tracks=''):
    return {name : title, 'tracks' : tracks}
answer = ''
while answer.lower() != 'q':
    name = input("Enter artist name\n> ")
    title = input("Enter album name\n> ")
    print(make_album(name, title))
    answer = input("Shall we continue? (Q?) ")
