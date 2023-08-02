class SequenceRepeat:
    def __init__(self, sequence: str, number: int):
        # Initialize the SequenceRepeat object with the given sequence and number
        self.sequence = sequence
        self.number = number
        self.current_index = -1

    def __iter__(self):
        # Return the iterator object itself
        return self

    def __next__(self):
        # Check if the current index is equal to the number minus one
        if self.current_index == self.number - 1:
            # If so, raise StopIteration to stop the iteration
            raise StopIteration
        # Increment the current index by 1
        self.current_index += 1
        # Return the character at the current index modulo the length of the sequence
        return self.sequence[self.current_index % len(self.sequence)]
