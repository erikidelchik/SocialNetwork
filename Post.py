# from matplotlib import pyplot as plt
# from matplotlib import image


class Post:

    def __init__(self, owner):
        self.owner = owner
        self.likes = 0

    def like(self, other):
        if type(other is type(self.owner)):
            self.likes += 1
            if other.username != self.owner.username:
                print(f"notification to {self.owner.username}: {other.username} liked your post")
                notification = f"{other.username} liked your post"
                self.owner.add_notification(notification)

    def comment(self, other, message):
        if type(other) is type(self.owner):
            if other.username != self.owner.username:
                print(f"notification to {self.owner.username}: {other.username} commented on your post: {message}")
                notification = f"{other.username} commented on your post"
                self.owner.add_notification(notification)


class TextPost(Post):
    def __init__(self, owner, text):
        super().__init__(owner)
        self.post_message = f'{self.owner.username} published a post:\n"{text}"\n'
        print(self.post_message)

    def __str__(self):
        return f'{self.post_message}'


class ImagePost(Post):
    def __init__(self, owner, img):
        super().__init__(owner)
        self.img = img
        print(f"{self.owner.username} posted a picture\n")

    def display(self):
        # img = image.imread(self.img)
        # plt.imshow(img)
        print("Shows picture")

    def __str__(self):
        return f"{self.owner.username} posted a picture\n"


class SalePost(Post):

    def __init__(self, owner, item, price, location):
        super().__init__(owner)
        self.price = price
        self.item = item
        self.location = location
        self.price = price
        self.on_sale = True
        print(f"{self.owner.username} posted a product for sale:")
        print(f"For sale! {item}, price: {price}, pickup from: {location}\n")

    def __str__(self):
        if not self.on_sale:
            return f"{self.owner.username} posted a product for sale:\nSold! {self.item}, price: {self.price}, pickup from: {self.location}\n"
        else:
            return f"{self.owner.username}'s product is on sale"

    def sold(self, password):
        if self.owner.password == password:
            self.on_sale = False
            print(f"{self.owner.username}'s product is sold")

    def discount(self, amount, password):
        if self.owner.password == password:
            self.price = self.price - self.price * amount / 100
            print(f"Discount on {self.owner.username} product! the new price is: {self.price}")
