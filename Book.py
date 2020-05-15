# Book class
#
# PDO class for the book information
class Book:
    title = None
    author = None
    category = None

    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return "Name: {}, Author: {}, Category: {}".format(self.title, self.author, self.category)
