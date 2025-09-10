from Models.UserModel import User


class UserController:
    def __init__(self):
        self.model = User()

    def register(self, username, password, role='customer'):
        return self.model.register(username, password, role)

    def login(self, username, password):
        return self.model.login(username, password)