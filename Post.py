from matplotlib import image, pyplot as plt


class Post:

    def __init__(self, owner, title, *args):
        self.title = title
        self.owner = owner
        self.args = args
        self.post = self.post_type()
        self.likes = 0

    def post_type(self):
        if self.title == "Text":
            return TextPost(self.owner, self.args[0])

        elif self.title == "Image":
            return ImagePost(self.owner, self.args[0])

        elif self.title == "Sale":
            return SalePost(self.owner, self.args[0], self.args[1], self.args[2])

    def like(self, other):
        if type(other is type(self.owner)):
            print(f"notification to {self.owner.username}: {other.username} liked your post")
            notification = f"{other.username} your post"
            self.owner.add_notification(notification)
            self.likes += 1

    def comment(self, other, message):
        if type(other) is type(self.owner):
            print(f"notification to {self.owner.username}: {other.username} commented on your post: {message}")
            notification = f"{other.username} commented on your post"
            self.owner.add_notification(notification)

    def discount(self, amount, password):
        self.post.discount(amount, password)

    def display(self):
        return self.post.display()

    def sold(self, password):
        return self.post.sold(password)

    def __str__(self):
        return str(self.post)


class TextPost:
    def __init__(self, owner, text):
        self.owner = owner
        self.text = text
        print(f"{self.owner.username} published a post:")
        print(self.text)

    def __str__(self):
        return self.text


class ImagePost:
    def __init__(self, owner, img):
        self.owner = owner
        self.img = img
        print(f"{self.owner.username} posted a picture")

    def display(self):
        # plt.imshow(self.img)
        pass

    def __str__(self):
        return "Image posted"


class SalePost:
    on_sale = True

    def __init__(self, owner, item, price, location):
        self.owner = owner
        self.price = price
        print(f"{self.owner.username} posted a product for sale:")
        print(f"For sale! {item}, price: {price}, pickup from: {location}")

    def __str__(self):
        if not self.on_sale:
            return f"{self.owner.username}'s product is sold"
        else:
            return f"{self.owner.username}'s product is on sale"

    def sold(self, password):
        if self.owner.password == password:
            self.on_sale = False

    def discount(self, amount, password):
        if self.owner.password == password:
            self.price = self.price-self.price*amount/100
            print(f"Discount on {self.owner.username} product! the new price is: {self.price}")
