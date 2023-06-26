# Define a class named Glass
class Glass:
    # Define a class variable named capacity and set its value to 250
    capacity = 250

    # Define the constructor method for the Glass class
    def __init__(self):
        # Initialize an instance variable named content to 0
        self.content = 0

    # Define a method named fill that takes an integer ml as input and returns a string
    def fill(self, ml: int) -> str:
        # Check if the sum of content and ml is greater than capacity
        if self.content + ml > Glass.capacity:
            # If true, return a string indicating that ml cannot be added to the glass
            return f'Cannot add {ml} ml'
        # If false, add ml to content
        self.content += ml
        # Return a string indicating that ml has been added to the glass
        return f'Glass filled with {ml} ml'

    # Define a method named empty that sets content to 0 and returns a string
    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    # Define a method named info that returns a string
    def info(self) -> str:
        # Calculate the amount of space left in the glass and return a string indicating the amount
        return f'{Glass.capacity - self.content} ml left'


# Create an instance of the Glass class
glass = Glass()
# Call the fill method on the glass instance with 100 as input and print the result
print(glass.fill(100))
# Call the fill method on the glass instance with 200 as input and print the result
print(glass.fill(200))
# Call the empty method on the glass instance and print the result
print(glass.empty())
# Call the fill method on the glass instance with 200 as input and print the result
print(glass.fill(200))
# Call the info method on the glass instance and print the result
print(glass.info())
