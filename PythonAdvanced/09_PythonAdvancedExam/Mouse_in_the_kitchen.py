import sys

sizes = sys.stdin.readline().strip().split(',')
rows = int(sizes[0])
columns = int(sizes[1])
matrix = [[''] * columns for _ in range(rows)]
rowStartPosition = 0
colStartPosition = 0
countOfCheese = 0

for row in range(rows):
    cols = sys.stdin.readline().strip()
    for col in range(columns):
        matrix[row][col] = cols[col]
        if cols[col] == 'M':
            rowStartPosition = row
            colStartPosition = col
        if cols[col] == 'C':
            countOfCheese += 1

command = sys.stdin.readline().strip()
while command != "danger":
    if command == "left":
        if colStartPosition - 1 >= 0:
            if matrix[rowStartPosition][colStartPosition - 1] == '*':
                matrix[rowStartPosition][colStartPosition - 1] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                colStartPosition -= 1
            elif matrix[rowStartPosition][colStartPosition - 1] == 'C':
                matrix[rowStartPosition][colStartPosition - 1] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                countOfCheese -= 1
                colStartPosition -= 1
            elif matrix[rowStartPosition][colStartPosition - 1] == 'T':
                matrix[rowStartPosition][colStartPosition - 1] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                colStartPosition -= 1
                print("Mouse is trapped!")
                break
            elif matrix[rowStartPosition][colStartPosition - 1] == '@':
                command = sys.stdin.readline().strip()
                continue
            elif matrix[rowStartPosition][colStartPosition - 1] == ' ':
                colStartPosition -= 1
        else:
            colStartPosition -= 1
            print("No more cheese for tonight!")
            break

    elif command == "right":
        if colStartPosition + 1 < columns:
            if matrix[rowStartPosition][colStartPosition + 1] == '*':
                matrix[rowStartPosition][colStartPosition + 1] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                colStartPosition += 1
            elif matrix[rowStartPosition][colStartPosition + 1] == 'C':
                matrix[rowStartPosition][colStartPosition + 1] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                countOfCheese -= 1
                colStartPosition += 1
            elif matrix[rowStartPosition][colStartPosition + 1] == 'T':
                matrix[rowStartPosition][colStartPosition + 1] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                colStartPosition += 1
                print("Mouse is trapped!")
                break
            elif matrix[rowStartPosition][colStartPosition + 1] == '@':
                command = sys.stdin.readline().strip()
                continue
            elif matrix[rowStartPosition][colStartPosition + 1] == ' ':
                colStartPosition += 1
        else:
            colStartPosition += 1
            print("No more cheese for tonight!")
            break

    elif command == "up":
        if rowStartPosition - 1 >= 0:
            if matrix[rowStartPosition - 1][colStartPosition] == '*':
                matrix[rowStartPosition - 1][colStartPosition] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                rowStartPosition -= 1
            elif matrix[rowStartPosition - 1][colStartPosition] == 'C':
                matrix[rowStartPosition - 1][colStartPosition] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                countOfCheese -= 1
                rowStartPosition -= 1
            elif matrix[rowStartPosition - 1][colStartPosition] == 'T':
                matrix[rowStartPosition - 1][colStartPosition] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                rowStartPosition -= 1
                print("Mouse is trapped!")
                break
            elif matrix[rowStartPosition - 1][colStartPosition] == '@':
                command = sys.stdin.readline().strip()
                continue
            elif matrix[rowStartPosition - 1][colStartPosition] == ' ':
                rowStartPosition -= 1
        else:
            rowStartPosition -= 1
            print("No more cheese for tonight!")
            break

    elif command == "down":
        if rowStartPosition + 1 < rows:
            if matrix[rowStartPosition + 1][colStartPosition] == '*':
                matrix[rowStartPosition + 1][colStartPosition] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                rowStartPosition += 1
            elif matrix[rowStartPosition + 1][colStartPosition] == 'C':
                matrix[rowStartPosition + 1][colStartPosition] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                countOfCheese -= 1
                rowStartPosition += 1
            elif matrix[rowStartPosition + 1][colStartPosition] == 'T':
                matrix[rowStartPosition + 1][colStartPosition] = 'M'
                matrix[rowStartPosition][colStartPosition] = '*'
                rowStartPosition += 1
                print("Mouse is trapped!")
                break
            elif matrix[rowStartPosition + 1][colStartPosition] == '@':
                command = sys.stdin.readline().strip()
                continue
            elif matrix[rowStartPosition + 1][colStartPosition] == ' ':
                rowStartPosition += 1
        else:
            rowStartPosition += 1
            print("No more cheese for tonight!")
            break

    if countOfCheese == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
        break

    command = sys.stdin.readline().strip()

if countOfCheese > 0 and command == "danger":
    print("Mouse will come back later!")

for row in matrix:
    print("".join(row))