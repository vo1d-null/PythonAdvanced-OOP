class DictionaryIter:
    def __init__(self, dictionary: dict):
        # Initialize the DictionaryIter object with the given dictionary
        self.dictionary = dictionary
        # Initialize the index to 0
        self.index = 0
        # Calculate the length of the dictionary and subtract 1
        self.length = len(self.dictionary) - 1
        # Convert the dictionary items into a list
        self.items = list(self.dictionary.items())

    def __iter__(self):
        # Return the DictionaryIter object itself as an iterator
        return self

    def __next__(self):
        # Check if the index is greater than the length
        if self.index > self.length:
            # Raise StopIteration to signal the end of iteration
            raise StopIteration()
        # Get the current index
        current_index = self.index
        # Increment the index by 1
        self.index += 1
        # Return the item at the current index
        return self.items[current_index]


# Create a DictionaryIter object with the given dictionary
result = DictionaryIter({1: "1", 2: "2"})
# Iterate over the DictionaryIter object and print each item
for item in result:
    print(item)
