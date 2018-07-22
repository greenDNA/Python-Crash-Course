class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age
    def describe_user(self):
        print("{} {} is {} years of age.".format(self.first_name, self.last_name, self.age))
    def greet_user(self):
        print("Hello {}, welcome.".format(self.first_name.title()))

class Admin(User):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)
        self.privileges = Privileges('text message')    

class Privileges:
    def __init__(self, privilege):
        self.privileges = [privilege]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

user1 = Admin('donald', 'glover', 22)
user2 = User('pikachu', 'ketchum', 1992)
user3 = User('sonic', 'hedghog', 1982)

user1.describe_user()
user1.greet_user()
user1.privileges.show_privileges()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
