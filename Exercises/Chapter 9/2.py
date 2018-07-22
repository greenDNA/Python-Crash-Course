class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is {} and serves {}.".format(self.name, self.cuisine))

    def open_restaurant(self):
        print("The restaurant is open.")

place = Restaurant('Red Lobster', 'Seafood')
place2 = Restaurant('Olive Garden', 'Italian')
place3 = Restaurant('McDonalds', 'American')

place.describe_restaurant()
place2.describe_restaurant()
place3.describe_restaurant()
