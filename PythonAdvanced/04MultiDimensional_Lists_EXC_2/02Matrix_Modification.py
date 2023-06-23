size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()

while command[0] != "END":
    type_comm, row, col, val = command[0], int(command[1]), int(command[2]), int(command[3])
    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")
    elif type_comm == "Add":
        matrix[row][col] += val
    elif type_comm == "Subtract":
        matrix[row][col] -= val

    command = input().split()

[print(*row) for row in matrix]
