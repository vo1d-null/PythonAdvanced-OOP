import itertools
import speech_recognition as sr
from collections import deque
from  pyfiglet import Figlet
from colorama import Fore

def get_name(player_number):
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print(f'{Fore.GREEN}Player {player_number} say your name:{Fore.RESET}')

            audio = r.record(source, duration=3)
            print(f'{Fore.YELLOW}Recognizing...{Fore.RESET}')
            try:
                return r.recognize_google(audio)
            except sr.UnknownValueError:
                print(f'{Fore.LIGHTRED_EX}Could not understand.Please say your name again.{Fore.RESET}')

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
        print(f"{Fore.LIGHTYELLOW_EX}{player_name} wins!{Fore.RESET}")
        print(f'{Fore.CYAN}Game length: {turns}{Fore.RESET}')
        raise SystemExit




def place_symbol(row, col):
    board[row][col] = players[0][1]

    check_win()

    print_board()

    if turns == SIZE**2:
        print(f"{Fore.LIGHTWHITE_EX}It's a tie!{Fore.RESET}")
        print(f'{Fore.MAGENTA}Game length: {turns}{Fore.RESET}')
        raise SystemExit

    players.rotate()



def choose_position():
    global turns

    while True:
        try:
            position = int(input(f'{Fore.LIGHTBLUE_EX}{players[0][0]} choose a free position in range [1-{SIZE**2}]: {Fore.RESET}'))
            row, col = (position -1) // SIZE, (position -1) % SIZE
        except ValueError:
            print(f'{Fore.LIGHTRED_EX}{players[0][0]} choose a valid position{Fore.RESET}')
            continue

        if 1 <= position <= SIZE**2 and board[row][col] == ' ':
            turns += 1
            place_symbol(row, col)
        else:
            print(f'{Fore.LIGHTRED_EX}{players[0][0]} choose a valid position!{Fore.RESET}')


def print_board(begin=False):
    if begin:
        print(f'{Fore.BLUE}This is the numeration of the board{Fore.RESET}')
        [print(f"{Fore.LIGHTCYAN_EX}| {' | '.join(row)} |{Fore.RESET}" ) for row in board]

        for row, col in itertools.product(range(SIZE), range(SIZE)):
            board[row][col] = " "
    else:
        [print(f"{Fore.LIGHTCYAN_EX}| {' | '.join(row)} |{Fore.RESET}" ) for row in board]



def start():
    figlet = Figlet(font='starwars',justify='left',width=300)
    print(figlet.renderText('Tic Tac Toe'))

    player_name_one = get_name('one')
    player_name_two = get_name('two')

    while True:
        player_sym_one = input(f"{Fore.LIGHTMAGENTA_EX}Player {player_name_one} choose between 'X' and 'O': {Fore.RESET}").upper()
        if player_sym_one in ['X', 'O']:
            break
        print(f"{Fore.LIGHTRED_EX}Invalid symbol!Enter 'X' or 'O'{Fore.RESET}")
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

# pip install requirements.txt


