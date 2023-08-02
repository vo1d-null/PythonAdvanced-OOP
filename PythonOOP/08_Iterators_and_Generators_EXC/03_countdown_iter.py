class CountdownIterator:
    def __init__(self, count):
        self.count = count
        self.end = 0
        self.last = self.count

    def __iter__(self):
        return self

    def __next__(self):
        # Check if the last value has reached the end value
        if self.last < self.end:
            raise StopIteration()
        # Store the current value
        current_value = self.last
        # Decrement the last value
        self.last -= 1
        # Return the current value
        return current_value


# Create an instance of the CountdownIterator class with count = 10
iterator = CountdownIterator(10)
# Iterate over the iterator and print each item
for item in iterator:
    print(item, end=" ")
