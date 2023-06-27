# This is a class for creating Task objects
class Task:
    # Constructor method to initialize the object with name, due date, comments and status
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    # Method to change the name of the task
    def change_name(self, new_name):
        # Check if the new name is the same as the current name
        if self.name == new_name:
            return "Name cannot be the same."
        # Update the name and return it
        self.name = new_name
        return self.name

    # Method to change the due date of the task
    def change_due_date(self, new_date):
        # Check if the new date is the same as the current date
        if self.due_date == new_date:
            return "Date cannot be the same."
        # Update the due date and return it
        self.due_date = new_date
        return self.due_date

    # Method to add a comment to the task
    def add_comment(self, comment):
        self.comments.append(comment)

    # Method to edit a comment in the task
    def edit_comment(self, comment_number, new_comment):
        # Check if the comment number is valid
        if comment_number < 0 or comment_number >= len(self.comments):
            return "Cannot find comment."
        # Update the comment and return all the comments
        self.comments[comment_number] = new_comment
        return ', '.join(self.comments)

    # Method to get the details of the task
    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
