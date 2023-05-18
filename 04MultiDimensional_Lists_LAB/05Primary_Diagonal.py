rows = int(input())

matrix = []

for _ in range(rows):
    inner = [int(el) for el in input().split()]
    matrix.append(inner)

sum_diag = 0
for i in range(rows):
    sum_diag += matrix[i][i]
print(sum_diag)