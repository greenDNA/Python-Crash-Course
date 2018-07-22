from random import Random
class Die:
    def __init__(self, sides = 6):
        self.sides = sides
        self.die = ''

    def roll_die(self):
        random = Random()
        self.die = random.randint(1, self.sides)
        print(self.die)

for index in range(1,11):
    Die(20).roll_die()#6,10,20 sides
