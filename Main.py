from Book import Book
from Library import Library
from Receipt import Receipt


# Main UI class for the system
#
# Create a new UI and holds the environmental variables for the
# program execution
class UI:
    lib = Library()
    receipt = Receipt()

    # Default constructor for the UI class
    def __init__(self):
        pass

    # UI for getting input for the Book object
    def add_book_prompt(self):
        self.lib.add_book(Book(input("Enter title: "), input("Enter author: "), input("Enter category: ")))

    # UI for getting input for search and adding book to receipt
    def search(self):
        param = input("Enter a string to search for: ")
        result = Menu(["Search by name", "Search by author", "Search by category"],
                      [self.lib.search_book_by_name, self.lib.search_book_by_author, self.lib.search_book_by_category],
                      [param]).show()

        if len(result) > 0:
            for i, book in zip(range(1, len(result) + 1), result):
                print(i, ". ", book, sep='')
            op = input('Do you want to add book to bucket [Y/n]: ')
            if op != 'n':
                try:
                    self.receipt.add_book(result[int(input('Enter book number: ')) - 1], input('Enter due date: '))
                except IndexError:
                    print('Invalid index: Restarting')

    # Wrapper method for the UI to call receipt function
    def print_receipt(self):
        self.receipt.generate_receipt()

    # Launches the UI
    def show(self):
        print('Library')
        Menu(["Add to library", "Search library", "Show receipt", "Exit"],
             [self.add_book_prompt, self.search, self.print_receipt, exit]).show()
        pass


# Menu class for the system
#
# Generates dynamic menu based on menu items and binds them to functions
class Menu:
    menu_items = []
    menu_funcs = []
    args = []

    def __init__(self, menu_items: list, menu_funcs: list, args: list = None):
        """
        Args:
            menu_items (list): list containing all the items
            menu_funcs (list): list containing all the functions for corresponding items
            args (list): list containing the arguments passed to functions
        """
        if len(menu_items) != len(menu_funcs):
            raise AssertionError('Size of menu items and funcs are not equal')
        self.menu_items = menu_items
        self.menu_funcs = menu_funcs
        self.args = args

    def show(self):
        """
        Function to show the generated menu
        :return: returns the result of the function called
        """
        size = len(self.menu_items)
        result = None
        for i, item in zip(range(size), self.menu_items):
            print('\t', i, ". ", item, sep='')

        x = int(input("Enter option: "))
        if x < size or x >= 0:
            if self.args is not None:
                result = self.menu_funcs[x](*self.args)
            else:
                result = self.menu_funcs[x]()

        return result


if __name__ == "__main__":
    ui = UI()
    while True:
        ui.show()
