cities = {
    'dallas' : {
        'country' : 'usa',
        'population' : '500000',
        'fact' : 'in texas'
    },
    'richmond' : {
        'country' : 'usa',
        'population' : '400000',
        'fact' : 'in virginia'
    },
    'seattle' : {
        'country' : 'usa',
        'population' : '100000',
        'fact' : 'in washington'
    }
}
for city, data in cities.items():
    print("In {} I know that".format(city))
    for key, value in data.items():
        print("{} is {}".format(key, value))
