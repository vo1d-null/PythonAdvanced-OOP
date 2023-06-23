def grocery_store(**groceries):
    groceries = sorted(groceries.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for grocery, quantity in groceries:
        result.append(f"{grocery}: {quantity}")
    return '\n'.join(result)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

