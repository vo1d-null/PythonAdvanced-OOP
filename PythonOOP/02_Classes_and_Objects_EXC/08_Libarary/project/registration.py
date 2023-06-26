from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        # check if user already exists in the library
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        # if not, add user to library user records
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        # check if user exists in the library
        if user not in library.user_records:
            return "We could not find such user to remove!"
        # if user exists, remove user from library user records
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        # iterate over library user records
        for user in library.user_records:
            # check if user id matches
            if user.user_id == user_id:
                # check if new username is already taken
                if user.username == new_username:
                    return "Please check again the provided username - it should be different " \
                           "than the username used so far!"
                # if not, update rented books with new username
                if user.username in library.rented_books:
                    rented_books = library.rented_books[user.username]
                    library.rented_books.pop(user.username)
                    library.rented_books[new_username] = rented_books
                # update user's username
                user.username = new_username
                # return success message
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        # if user id doesn't match, return error message
        return f"There is no user with id = {user_id}!"
