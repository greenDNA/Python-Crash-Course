identity = {
    'first_name' : 'george',
    'last_name' : 'michaels',
    'age' : '14',
    'city' : 'loyola'
    }
identity2 = {
    'first_name' : 'pam',
    'last_name' : 'michaels',
    'age' : '24',
    'city' : 'vlata'
}
identity3 = {
    'first_name' : 'orge',
    'last_name' : 'els',
    'age' : '34',
    'city' : 'orio'
}

people = [identity, identity2, identity3]

for person in people:
    for trait, value in person.items():
        print("I know that your {} is: {}".format(trait, value))
