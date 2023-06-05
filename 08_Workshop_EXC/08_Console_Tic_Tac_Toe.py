import itertools
from collections import deque

def check_win():
    player_name, player_sym = players[0]

    first_diagonal_win = all(board[i][i] == player_sym for i in range(SIZE))
    second_diagonal_win = all(board[i][SIZE - i - 1] == player_sym for i in range(SIZE))

    row_win = any(
        all(player_sym == pos for pos in row)
        for row in board
    )
    col_win = any(
        all(board[r][c] == player_sym for r in range(SIZE))
        for c in range(SIZE)
    )

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} wins!")
        print('Game length:', turns)
        raise SystemExit




def place_symbol(row, col):
    board[row][col] = players[0][1]

    check_win()

    print_board()

    if turns == SIZE**2:
        print("It's a tie!")
        print('Game length:', turns)
        raise SystemExit

    players.rotate()



def choose_position():
    global turns

    while True:
        try:
            position = int(input(f'{players[0][0]} choose a free position in range [1-{SIZE**2}]: '))
            row, col = (position -1) // SIZE, (position -1) % SIZE
        except ValueError:
            print(f'{players[0][0]} choose a valid position')
            continue

        if 1 <= position <= SIZE**2 and board[row][col] == ' ':
            turns += 1
            place_symbol(row, col)
        else:
            print(f'{players[0][0]} choose a valid position!')


def print_board(begin=False):
    if begin:
        print('This is the numeration of the board')
        [print(f"| {' | '.join(row)} |" ) for row in board]

        for row, col in itertools.product(range(SIZE), range(SIZE)):
            board[row][col] = " "
    else:
        [print(f"| {' | '.join(row)} |" ) for row in board]



def start():
    print("Welcome to Tic Tac Toe!")
    player_name_one = input("Player 1 enter your name: ")
    player_name_two = input("Player 2 enter your name: ")

    while True:
        player_sym_one = input(f"Player {player_name_one} choose between 'X' and 'O': ").upper()
        if player_sym_one in ['X', 'O']:
            break
        print("Invalid symbol!Enter 'X' or 'O'")
        continue

    player_sym_two = 'O' if player_sym_one == 'X' else 'X'
    players.append([player_name_one, player_sym_one])
    players.append([player_name_two, player_sym_two])

    print_board(begin=True)
    choose_position()



SIZE = 3
turns = 0

board = [[str(i), str(i+1), str(i+2)] for i in range(1, SIZE**2 + 1, SIZE)]

players = deque()
start()



