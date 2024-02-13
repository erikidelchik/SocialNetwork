class Observer:

    def notify(self):
        pass


class PostObserver(Observer):
    def __init__(self, owner):
        self.owner = owner
        self.username = owner.username

    def notify(self):
        for follower in self.owner.followers:
            follower.add_notification(f"{self.username} has a new post")

# class likes_observer(observer):
#     def __init__(self,other):
#         self.other = other
#
#     def notify(self):
#             self.owner.add_notification(f"{self.other} liked your post")
#
#
# class comments_observer(observer):
#     def __init__(self,other):
#         self.other = other
#
#     def notify(self):
#         self.owner.add_notification(f"{self.other.username} commented on your post")
