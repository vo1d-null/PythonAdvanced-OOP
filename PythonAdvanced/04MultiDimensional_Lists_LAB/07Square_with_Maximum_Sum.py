rows, cols = [int(el) for el in input().split(', ')]

matrix = []
for _ in range(rows):
    inner = [int(el) for el in input().split(', ')]
    matrix.append(inner)

max_sum = float('-inf')
sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        curr_el = matrix[row][col]
        below_el = matrix[row + 1][col]
        next_el = matrix[row][col + 1]
        diag_el = matrix[row + 1][col + 1]
        sum_els = curr_el + below_el + next_el + diag_el

        if max_sum < sum_els:
            max_sum = sum_els
            sub_matrix = [[curr_el, next_el], [below_el, diag_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)