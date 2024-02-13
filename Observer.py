class Observer:

    def notify(self):
        pass


class PostNotificationObserver(Observer):
    def __init__(self, owner):
        self.owner = owner
        self.username = owner.username

    def notify(self):
        for follower in self.owner.followers:
            follower.add_notification(f"{self.username} has a new post")


# class LikesNotificationObserver(Observer):
#     def __init__(self, owner, other):
#         self.owner = owner
#         self.other = other
#
#     def notify(self):
#         self.owner.add_notification(f"{self.other} liked your post")
#
#
# class CommentsNotificationObserver(Observer):
#     def __init__(self, owner, other):
#         self.owner = owner
#         self.other = other
#
#     def notify(self):
#         self.owner.add_notification(f"{self.other.username} commented on your post")
