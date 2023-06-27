# This class represents a section that contains tasks
class Section:
    # Constructor that initializes the section name and an empty list of tasks
    def __init__(self, name):
        self.name = name
        self.tasks = []

    # Method to add a task to the section
    def add_task(self, task):
        # Check if the task is already in the section
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        # Add the task to the section and return a message
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    # Method to mark a task as completed
    def complete_task(self, task_name):
        # Iterate through the tasks in the section
        for task in self.tasks:
            # Check if the task matches the given name
            if task.name == task_name:
                # Mark the task as completed and return a message
                task.completed = True
                return f"Completed task {task_name}"
        # If the task is not found, return a message
        return f"Could not find task with the name {task_name}"

    # Method to remove completed tasks from the section
    def clean_section(self):
        # Get the initial length of the task list
        initial_length = len(self.tasks)
        # Create a new list of tasks that are not completed
        self.tasks = [task for task in self.tasks if not task.completed]
        # Return a message with the number of tasks removed
        return f"Cleared {initial_length - len(self.tasks)} tasks."

    # Method to view the tasks in the section
    def view_section(self):
        # Create a string with the section name
        result = f"Section {self.name}:\n"
        # Iterate through the tasks and add their details to the string
        for task in self.tasks:
            result += f"{task.details()}\n"
        # Return the string with the tasks
        return result.strip()
