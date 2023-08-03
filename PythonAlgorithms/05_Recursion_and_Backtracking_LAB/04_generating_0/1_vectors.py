def gen_vector(vector, idx):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[idx] = num

        gen_vector(vector, idx + 1)


vector_size = int(input())
vector = [None] * vector_size

gen_vector(vector, 0)