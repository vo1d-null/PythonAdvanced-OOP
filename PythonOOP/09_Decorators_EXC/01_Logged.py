def logged(function):
    def wrapper(*args):
        # Construct the message with the function name and arguments
        message = f"you called {function.__name__}({', '.join(str(arg) for arg in args)})\n"
        # Call the function and get the result
        result = function(*args)
        # Append the result to the message
        message += f"it returned {result}"
        return message


    return wrapper


@logged
def func(*args):
    return 3 + len(args)


# Call the decorated function
print(func(4, 4, 4))
