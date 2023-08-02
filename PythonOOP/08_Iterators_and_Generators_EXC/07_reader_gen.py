def read_next(*args):
    # Iterate over each element in args
    for el in args:
        # If element is a string or tuple, yield each character or element respectively
        if isinstance(el, (str, tuple)):
            yield from el
        elif isinstance(el, dict):
            yield from el.keys()


# Iterate over each item yielded by read_next function
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    # Print each item without a new line
    print(item, end='')
