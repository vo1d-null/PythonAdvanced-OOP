rows, cols = [int(el) for el in input().split(', ')]

matrix = []
for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

col_sums = []
for col_index in range(cols):
    sum_col_els = 0
    for row_index in range(rows):
        sum_col_els += matrix[row_index][col_index]
    col_sums.append(sum_col_els)

for col_sum in col_sums:
    print(col_sum)
