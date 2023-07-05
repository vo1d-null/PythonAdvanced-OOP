# Importing the Animal class from the project.animal module
from project.animal import Animal


# Defining the Cat class that inherits from the Animal class
class Cat(Animal):
    # Defining the meow method
    def meow(self):
        # Returning the string "meowing..."
        return "meowing..."
