def cache(func):
    # This function is a decorator that caches the results of the decorated function.
    def wrapper(num):
        # Check if the result for the given argument is already cached
        if num not in wrapper.log:
            # If not, calculate the result and cache it
            wrapper.log[num] = func(num)
        # Return the cached result
        return wrapper.log[num]

    # Initialize an empty dictionary to store the cached results
    wrapper.log = {}
    # Return the wrapper function
    return wrapper


@cache
def fibonacci(n):
    # Calculate the nth Fibonacci number recursively
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


# Calculate the 5th Fibonacci number
fibonacci(5)
# Print the cached results
print(fibonacci.log)
