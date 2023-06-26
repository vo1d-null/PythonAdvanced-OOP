# Importing User class from project.user module
from project.user import User


# Defining Library class
class Library:
    def __init__(self):
        # Initializing user_records, books_available and rented_books instance variables
        self.user_records = []  # this list will store user objects
        self.books_available = {}
        self.rented_books = {}

    # Method to rent a book
    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        # Checking if the book is available
        if author in self.books_available and book_name in self.books_available[author]:
            # Adding the book to user's books and removing it from available books
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            # Adding the book to user's rented books
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            # Returning success message
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        # Checking if the book is already rented
        for user_books in self.rented_books.values():
            if book_name in user_books:
                return f'The book "{book_name}" is already rented and will be available in ' \
                       f'{user_books[book_name]} days!'

    # Method to return a book
    def return_book(self, author: str, book_name: str, user: User):
        # Checking if the user has the book
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        # Removing the book from user's books and adding it to available books
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        # Removing the book from user's rented books
        self.rented_books[user.username].pop(book_name)
