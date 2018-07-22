class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("{} {} is {} years of age.".format(self.first_name, self.last_name, self.age))

    def greet_user(self):
        print("Hello {}, welcome.".format(self.first_name.title()))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('donald', 'glover', 22)
user2 = User('pikachu', 'ketchum', 1992)
user3 = User('sonic', 'hedghog', 1982)

user1.increment_login_attempts()
print(user1.login_attempts)
