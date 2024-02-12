from Post import *


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._online = True
        self.following = []
        self.followers = []
        self.notifications = []
        self.posts_number = 0

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
            other.followers.remove(self)
            print(f"{self.username} unfollowed {other.username}")

    def publish_post(self, title, *args):
        if self._online:
            new_post = None
            if title == "Text":
                new_post = TextPost(self, *args)
            elif title == "Image":
                new_post = ImagePost(self, *args)
            elif title == "Sale":
                new_post = SalePost(self, *args)

            if new_post is not None:
                for other in self.followers:
                    other.add_notification(f"{self.username} has a new post")
                self.posts_number += 1
                return new_post

    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.notifications:
            print(f"{notification}")

    def add_notification(self, notification):
        self.notifications.append(notification)

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {self.posts_number}, Number of followers: {len(self.followers)}"
