rows = int(input())

char_matrix = []
for _ in range(rows):
    inner = list(input())
    char_matrix.append(inner)

sym = input()
pos = None
for i in range(rows):
    if pos:
        break
    for j in range(rows):
        if char_matrix[i][j] == sym:
            pos = (i, j)
            break

if pos:
    print(pos)
else:
    print(f"{sym} does not occur in the matrix")