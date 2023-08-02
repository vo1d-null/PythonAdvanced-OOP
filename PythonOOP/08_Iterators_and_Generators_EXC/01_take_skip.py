class TakeSkip:
    def __init__(self, step: int, count: int):
        self.step = step  # The step size
        self.count = count  # The total number of elements
        self.i = 0  # The current index

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.count:  # If the current index exceeds the total number of elements
            raise StopIteration()  # Stop the iteration
        i = self.i  # Store the current index
        self.i += 1  # Increment the index for the next iteration
        return i * self.step  # Return the current element
# Usage example:
# numbers = TakeSkip(2, 6)  # Create an instance of TakeSkip with a step size of 2 and a count of 6
# for number in numbers:  # Iterate over the elements
#     print(number)  # Print each element
