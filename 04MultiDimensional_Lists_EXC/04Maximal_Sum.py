rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = float('-inf')

max_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        sec_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        curr_sum = sum(first_row) + sum(sec_row) + sum(third_row)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_matrix = [first_row, sec_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in max_matrix]


