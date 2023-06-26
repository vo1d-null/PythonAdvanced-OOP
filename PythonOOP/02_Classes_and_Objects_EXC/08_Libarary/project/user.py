# This class represents a user with an ID, username, and a list of books they own
class User:
    def __init__(self, user_id: int, username: str):
        # Initialize the user with their ID, username, and an empty list of books
        self.user_id = user_id
        self.username = username
        self.books = []

    # Returns a string of the user's books sorted alphabetically
    def info(self):
        return ', '.join(sorted(self.books))

    # Returns a string representation of the user's ID, username, and list of books
    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
