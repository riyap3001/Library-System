from datetime import date

import Book


# Receipt class
#
# Class to generate the receipt
class Receipt:
    books = []

    def add_book(self, book: Book, due_date=date.today()):
        self.books.append([book, due_date])

    def remove_book(self, book: Book):
        self.books.remove(book)

    def generate_receipt(self):
        print("Receipt")
        for book, due_date in self.books:
            print(book)
            print("Due date: ", due_date)
