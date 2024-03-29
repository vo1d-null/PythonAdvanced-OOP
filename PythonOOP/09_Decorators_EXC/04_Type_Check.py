def type_check(func_type):
    def decorator(function):
        def wrapper(*args):
            # Check if each argument is of the specified type
            for arg in args:
                if not isinstance(arg, func_type):
                    return "Bad Type"
            # If all arguments are of the specified type, call the original function
            return function(*args)

        return wrapper

    return decorator
#
# @type_check(int)
# def times2(num):
#     return num * 2
#
#
# print(times2(2))
# print(times2('Not A Number'))
#
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
#
# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))
