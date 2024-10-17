'''

1. Start
    - Choose Difficulty (?)
2. Display Empty Board
    - like this:

          |     |
       1  |  2  |  3
     _____|_____|_____
          |     |
       4  |  5  |  6
     _____|_____|_____
          |     |
       7  |  8  |  9
          |     |

3. Ask for user input (1-9) and mark square
4. Computer marks square
5. If winner, show winner
6. if full, show tie
7. if neither, goto 2
8. ask to play again?
9. if yes goto 1
10. end

'''
import random

DOUBLE_BAR = '| \u2588   \u2588 '
SINGLE_BAR = '|   \u2588   '
EMPTY = '|       '

def initialize_board()->list:
    return [
    ['1',
    '2',
    '3'],
    ['4',
    '5',
    '6'],
    ['7',
    '8',
    '9']
]


def send(message:str)->None:
    print(f'==> {message}')


def ask(question:str)->str:
    return input(f'==> {question}')


def is_valid_choice(bs:list, val:int)->bool:
    return bs[val // 3][val % 3] not in 'XO'


def get_square(bs:list)->list:
    new_state = bs.copy()
    while True:
        try:
            val = int(ask('Choose a Square! ')) - 1 # Put in index terms
            if 9 > val >= 0 and is_valid_choice(bs, val):
                new_state[val // 3][val % 3] = 'X'
                return new_state
            else:
                send('Please Choose a Valid Number 1-9')
        except ValueError:
            send('Please Choose a Valid Number 1-9')


def easy_bot(bs:list)->list:
    new_state = bs.copy()
    options = [index for index, _
               in enumerate([item for sublist in bs for item in sublist])
               if is_valid_choice(bs, index)]

    choice = random.choice(options)
    new_state[choice // 3][choice % 3] = 'O'
    return new_state


def is_over(bs:list):
    pass


def make_board(bs: list)->str:
    fancy_board = ''
    for index, row in enumerate(bs):
        fancy_board += make_row(index, row)
        if index + 1 != len(bs):
            fancy_board += '\n+-------+-------+-------+\n'
    return fancy_board


def make_row(number, row:list)->str:
    fancy_row = ''
    for line in range(1,4):
        for index, item in enumerate(row):
            if item == 'X':
                fancy_row += SINGLE_BAR if line % 2 == 0 \
                    else DOUBLE_BAR

            elif item == 'O':
                fancy_row += DOUBLE_BAR if line % 2 == 0 \
                    else SINGLE_BAR

            else:
                if line % 2 == 0:
                    fancy_row += f'|   {number * len(row) + index + 1}   '
                else:
                    fancy_row += EMPTY

        fancy_row += '|\n' if line % 3 else '|'

    return fancy_row


def find_winner(bs:list)->tuple:
    to_check = ['X', 'O']
    for check in to_check:
        # find row
        if all([item == check for item in bs[0]]):
            send('X WINS!')
            return True, check
        # find column
        




def run_game():
    board_state = initialize_board()
    print(make_board(board_state))
    winner = False
    while not winner:
        board_state = get_square(board_state)
        board_state = easy_bot(board_state)
        print(make_board(board_state))
        winner = find_winner(board_state)
    if ask('Again?'):
        run_game()

run_game()