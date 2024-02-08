class User:
    _online = False
    following = []
    followers = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.online = True

    def __eq__(self, other):
        return self.username == other.username and self.password == other.password

    def go_online(self):
        self._online = True

    def go_offline(self):
        self._online = False

    def follow(self, other):
        if self._online and other not in self.following:
            self.following.append(other)
            other.followers.append(self)
            print(f"{self.username} started following {other.username}")

    def unfollow(self, other):
        if self._online and other in self.following:
            self.following.remove(other)
