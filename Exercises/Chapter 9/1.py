class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is {} and serves {}.".format(self.name, self.cuisine))

    def open_restaurant(self):
        print("The restaurant is open.")

place = Restaurant('Red Lobster', 'Seafood')
print("{}\n{}".format(place.name, place.cuisine))
place.describe_restaurant()
place.open_restaurant()
