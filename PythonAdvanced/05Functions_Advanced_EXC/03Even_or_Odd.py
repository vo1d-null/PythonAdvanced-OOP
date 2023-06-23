def even_odd(*args):
    command = args[-1]

    if command == 'even':
        return [arg for arg in args[:-1] if int(arg) % 2 == 0]
    else:
        return [arg for arg in args[:-1] if int(arg) % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))