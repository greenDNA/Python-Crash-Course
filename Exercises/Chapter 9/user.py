class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age
    def describe_user(self):
        print("{} {} is {} years of age.".format(self.first_name, self.last_name, self.age))
    def greet_user(self):
        print("Hello {}, welcome.".format(self.first_name.title()))
