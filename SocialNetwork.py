from User import User


class SocialNetwork:
    _instance = None
    _users = []

    def __new__(cls, network_name):
        if not cls._instance:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.network_name = network_name
            print(f"The social network {network_name} was created!")
        return cls._instance

    def __str__(self):
        return self.network_name

    def sign_up(self, name, password):
        # check if new_user not already exist
        for user in self._users:
            if user.username == name:
                return
        if 4 <= len(password) <= 8:
            new_user = User(name, password)
            self._users.append(new_user)
            return new_user

    def log_in(self, name, password):
        for user in self._users:
            if user.username == name and user.password == password:
                print(f"{user.username} connected")
                user.go_online()

    def log_out(self, name):
        for user in self._users:
            if user.username == name:
                print(f"{user.username} disconnected")
                user.go_offline()




# instance = SocialNetwork('Twitter')
# print(instance)
