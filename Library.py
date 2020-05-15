import pickle

import Book


# Library class for the system
#
# Class to hold the books info and load and store to hard drive
class Library:
    filename = "data.bin"

    books = []
    borrowed = []

    def __init__(self):
        self.load()

    def add_book(self, book: Book):
        """
        Function to add a new book to library

        :param book: The book that is to be added to library
        :return: None
        """
        self.books.append(book)
        self.save()

    def search_book_by_name(self, name: str):
        """
        Function to get list of books that have matching name

        :param name:
        :return: book list of that matches that name
        """
        result = []
        for book in self.books:
            if name in book.title:
                result.append(book)
        self.print_book_list(result)
        return result

    def search_book_by_author(self, author):
        """
        Function to get list of books that have matching author
        :param author:
        :return: book list of that matches that author
        """
        result = []
        for book in self.books:
            if author in book.author:
                result.append(book)
        self.print_book_list(result)
        return result

    def search_book_by_category(self, category):
        """
        Function to get list of books that have matching category
        :param category:
        :return: book list of that matches that category
        """
        result = []
        for book in self.books:
            if category in book.category:
                result.append(book)
        self.print_book_list(result)
        return result

    def save(self):
        """
        Function to flush contents to hard disk
        :return: None
        """
        pickle.dump(self, open(self.filename, "bw"))

    def load(self):
        """
        Function to load contents from hard disk to program
        :return: None
        """
        try:
            lib = pickle.load(open(self.filename, "br"))
            self.books = lib.books
            self.borrowed = lib.borrowed
        except IOError:
            pass

    @staticmethod
    def print_book_list(lst):
        """
        Function to print the book list
        :param lst: list containing books
        :return: None
        """
        for book in lst:
            print(book)
