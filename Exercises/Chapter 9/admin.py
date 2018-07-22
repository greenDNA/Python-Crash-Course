from privileges import Privileges
from user import User
class Admin(User):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)
        self.privileges = Privileges('text message')
