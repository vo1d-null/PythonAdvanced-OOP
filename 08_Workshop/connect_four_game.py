import operator

from collections import deque
from colorama import Fore

def print_board():
    [print(f"[{', '.join(row)}]") for row in board]

def place_circle():
    row = 0

    while row != ROWS and board[row][player_col] == '0':
        row += 1
    board[row -1][player_col] = player_sym
    return row -1

def get_circles_count(row, col, dx, dy, operator_func):
    current_count = 0

    for i in range(1, 4):
        new_row = operator_func(row, dx * i)
        new_col = operator_func(col, dy * i)

        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            break
        if board[new_row][new_col] != player_sym:
            break
        current_count += 1

    return current_count



def check_for_win(row, col):
    for x, y in directions:
        counter = get_circles_count(row, col, x, y, operator.add) + get_circles_count(row, col, x, y, operator.sub) + 1

        if counter >= 4:
            return True

    if counter_for_draw == ROWS * COLS:
        print_board()
        print("WOW...It's a Draw!")
        raise SystemExit

    return False

ROWS, COLS = 6, 7
counter_for_draw = 0

board = [['0'] * COLS for _ in range(ROWS)]

player_one_sym = f'{Fore.BLUE}1{Fore.RESET}'
player_two_sym = f'{Fore.LIGHTRED_EX}2{Fore.RESET}'

turns = deque([[1,player_one_sym],[2,player_two_sym]])

win = False

directions = ( (-1,0), #up
               (0,-1), #left
               (-1,-1), #up-left
               (1,1) #up-right
               )

while not win:
    print_board()
    player_num, player_sym = turns[0]

    try:
        player_col = int(input(f"Player {player_num} choose a column:")) -1
    except ValueError:
        print(f"{Fore.RED}Select a valid number between 1 and {COLS} {Fore.RESET}")
        continue

    if not 0 <= player_col < COLS:
        print(f"{Fore.RED}Select a valid number between 1 and {COLS} {Fore.RESET}")
        continue

    if board[0][player_col] != '0':
        print(f"{Fore.RED}Column {player_col} is full.Select another column!{Fore.RESET}")
        continue

    row = place_circle()
    counter_for_draw += 1
    win = check_for_win(row, player_col)

    turns.rotate()

print_board()
print(f"Player {turns[1][0]} wins!")

