def reverse_array(idx, array):
    if idx == len(array) // 2:
        return print(' '.join(array))

    array[idx], array[-idx - 1] = array[-idx - 1], array[idx]
    reverse_array(idx + 1, array)


array = [x for x in input().split(' ')]
reverse_array(0, array)