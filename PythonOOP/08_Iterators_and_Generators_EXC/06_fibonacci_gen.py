# Define a generator function for Fibonacci sequence
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Create a generator object from the fibonacci function
fib_gen = fibonacci()
# Print the first 5 numbers in the Fibonacci sequence
for _ in range(5):
    print(next(fib_gen))
# Reinitialize the generator object
fib_gen = fibonacci()
# Print only the first number in the Fibonacci sequence
for _ in range(1):
    print(next(fib_gen))
