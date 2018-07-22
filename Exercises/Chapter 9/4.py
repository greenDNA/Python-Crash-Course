class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is {} and serves {}.".format(self.name, self.cuisine))

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self):
        self.number_served += 1

restaurant = Restaurant('Red Lobster', 'Seafood')
print(restaurant.number_served)
restaurant.increment_number_served()
print(restaurant.number_served)
restaurant.set_number_served(23)
print(restaurant.number_served)
