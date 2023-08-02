def solution():
    def integers():
        # Initialize i to 1
        i = 1
        while True:
            # Generate the next integer
            yield i
            # Increment i by 1
            i += 1

    def halves():
        for i in integers():
            # Generate the next half of the integer
            yield i / 2

    def take(n, seq):
        # Generate a list of the next n elements from the sequence
        return [next(seq) for _ in range(n)]

    # Return the functions take, halves, and integers
    return (take, halves, integers)


# Get the take function from the solution
take = solution()[0]
# Get the halves function from the solution
halves = solution()[1]
# Print the first 5 halves of the integers
print(take(5, halves()))
