# Import the Person class from the project module
from project.person import Person


# Define a Child class that inherits from the Person class
class Child(Person):
    def __init__(self, name, age):
        # Call the parent class constructor using super()
        super().__init__(name, age)
