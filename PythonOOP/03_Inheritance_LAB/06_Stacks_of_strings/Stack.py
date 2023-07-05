from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, item):
        # Add item to the top of the stack
        self.data.append(item)

    def pop(self) -> str:
        # Remove and return the item from the top of the stack
        return self.data.pop()

    def top(self) -> str:
        # Return the item from the top of the stack without removing it
        return self.data[-1]

    def is_empty(self):
        # Check if the stack is empty
        return len(self.data) == 0

    def __str__(self):
        # Return a string representation of the stack
        return f"[{', '.join(list(self.data[::-1]))}]"

# The given code defines a class called "Stack" which represents a stack data structure. The stack is implemented using a list. The code provides methods to push an item onto the stack, pop an item from the top of the stack, get the top item without removing it, check if the stack is empty, and get a string representation of the stack.
#  Here is a step-wise explanation of the code:
#  1. The code imports the "List" type from the "typing" module. This is used to specify the type of the "data" attribute in the class.
#  2. The "Stack" class is defined with an __init__ method. This method initializes the "data" attribute as an empty list.
#  3. The "push" method takes an item as an argument and appends it to the end of the "data" list, effectively adding it to the top of the stack.
#  4. The "pop" method removes and returns the last item from the "data" list, which represents the item at the top of the stack.
#  5. The "top" method returns the last item from the "data" list without removing it, effectively returning the item at the top of the stack.
#  6. The "is_empty" method checks if the "data" list is empty by comparing its length to 0. It returns True if the stack is empty, and False otherwise.
#  7. The "__str__" method returns a string representation of the stack. It converts the "data" list into a reversed list, joins the elements with commas, and encloses them in square brackets.
