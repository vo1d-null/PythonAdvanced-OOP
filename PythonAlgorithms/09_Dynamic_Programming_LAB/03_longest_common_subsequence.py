first_str = input()
second_str = input()

rows = len(first_str) + 1
cols = len(second_str) + 1

result_matrix = []
[result_matrix.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):

        if first_str[row - 1] == second_str[col - 1]:
            result_matrix[row][col] = result_matrix[row - 1][col - 1] + 1

        else:
            result_matrix[row][col] = max(result_matrix[row - 1][col], result_matrix[row][col - 1])

print(result_matrix[rows - 1][cols - 1])
