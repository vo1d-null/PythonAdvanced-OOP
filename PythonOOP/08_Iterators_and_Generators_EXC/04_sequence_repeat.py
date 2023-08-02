class sequence_repeat:
    zero_index = -1

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current_index = self.zero_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == self.number - 1:
            raise StopIteration
        self.current_index += 1
        return self.sequence[self.current_index % len(self.sequence)]