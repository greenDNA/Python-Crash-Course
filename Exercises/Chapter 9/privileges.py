class Privileges:
    def __init__(self, privilege):
        self.privileges = [privilege]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
