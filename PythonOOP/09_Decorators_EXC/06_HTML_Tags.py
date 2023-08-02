# Define a function that returns a decorator
def tags(tag):
    # Define the decorator that returns a wrapper function
    def decorator(function):
        # Define the wrapper function that returns the decorated function with the tag
        def wrapper(*args):
            return f"<{tag}>{function(*args)}</{tag}>"

        return wrapper

    # Return the decorator
    return decorator


# Decorate the function with the 'p' tag
@tags('p')
def join_strings(*args):
    return "".join(args)


# Print the decorated function
print(join_strings("Hello", " you!"))


# Decorate the function with the 'h1' tag
@tags('h1')
def to_upper(text):
    return text.upper()


# Print the decorated function
print(to_upper('hello'))
