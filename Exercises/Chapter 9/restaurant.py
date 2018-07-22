class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is {} and serves {}.".format(self.name, self.cuisine))

    def open_restaurant(self):
        print("The restaurant is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        #super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

IceCreamStand('McDonald', 'America').display_flavors()
