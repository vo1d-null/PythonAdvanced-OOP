rows, cols = [int(x) for x in input().split(', ')]
matrix = []
result = 0
for row in range(rows):
    lines = [int(x) for x in input().split(', ')]
    result += sum(lines)
    matrix.append(lines)

print(result)
print(matrix)