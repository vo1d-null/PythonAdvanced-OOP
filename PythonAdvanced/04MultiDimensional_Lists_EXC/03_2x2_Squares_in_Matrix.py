rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for row in range(rows)]
eq_blocks = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol_x = matrix[row][col]

        if matrix[row][col + 1] == symbol_x \
                and matrix[row + 1][col] == symbol_x \
                and matrix[row + 1][col + 1] == symbol_x:
            eq_blocks += 1

print(eq_blocks)
