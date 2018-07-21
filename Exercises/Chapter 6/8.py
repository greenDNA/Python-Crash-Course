lucky = {
    'animal' : 'dog',
    'owner' : 'joe'
}
gato = {
    'animal' : 'cat',
    'owner' : 'tray'
}
pets = [lucky, gato]
for pet in pets:
    for trait, value in pet.items():
        print("I know that your {} is: {}".format(trait, value))
