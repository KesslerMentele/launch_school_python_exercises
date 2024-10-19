"""

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

"""
import random
import os
from copy import deepcopy

DOUBLE_BAR = '| \u2588   \u2588 '
SINGLE_BAR = '|   \u2588   '
EMPTY = '|       '
NUMBER = '|   {}   '
SPACER = '\n+-------+-------+-------+\n'
WIN_LINE = '\033[32m\u2588\033[0m'

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

#  I/O
def say(message:str)->None:
    print(f'==> {message}')


def ask(question:str)->str:
    return input(f'==> {question}')


def is_valid_choice(bs:list, val:int)->bool:
    return bs[val // 3][val % 3] not in 'XO'


def get_square(bs:list)->list:
    new_state = deepcopy(bs)
    options = get_options(bs)
    options = [val + 1 for val in options] # move out of index to count
    while True:
        try:
            say(f'Choose a Square! ({join_or(options, ", ", "or")})')
            val = int(ask(' ')) - 1 # Put in index terms
            if 9 > val >= 0 and is_valid_choice(bs, val):
                new_state[val // 3][val % 3] = 'X'
                return new_state
            else:
                say('Please Choose a Valid Number: ' + join_or(options,', ', 'or'))
        except ValueError:
            say('Please Choose a Valid Number' + join_or(options,', ', 'or'))


def print_board(bs:list)->None:
    print(''.join([row for sub_list in make_board(bs)
                   for row in sub_list]))


def print_with_win_line(bs:list, line_location:dict)->None:
    os.system('clear')
    print(''.join([row for sub_list in add_win_line(bs, line_location)
                   for row in sub_list]))


# Bot(s)
def easy(bs:list)->list:
    new_state = deepcopy(bs)
    options = get_options(bs)

    option = random.choice(options)
    new_state[option // 3][option % 3] = 'O'
    return new_state


def necessary_move(bs, options):
    for option in options:
        my_play = deepcopy(bs)
        my_play[option // 3][option % 3] = 'O'
        has_won = find_winner(my_play)
        if has_won['win'] and has_won['winner'] == 'O':
            return my_play
    for option in options:
        their_play = deepcopy(bs)
        their_play[option // 3][option % 3] = 'X'
        has_won = find_winner(their_play)
        if has_won['win'] and has_won['winner'] == 'X':
            their_play = deepcopy(bs)
            their_play[option // 3][option % 3] = 'O'
            return their_play
    return None


def medium(bs:list)->list:
    options = get_options(bs)
    need = necessary_move(bs, options)
    new_state = deepcopy(bs)
    if need:
        return need
    return easy(bs)


def hard(bs:list)->list:
    options = get_options(bs)
    need = necessary_move(bs, options)
    new_state = deepcopy(bs)
    if need:
        return need
    if 4 in options:
        new_state[1][1] = 'O'
        return new_state
    return easy(bs)


# Board Construction
def make_board(bs: list)->list:
    fancy_board = []

    def make_row(number, r: list) -> list:
        fancy_row_full = []
        # Loop for each row of the board
        for line in range(1, 4):
            fancy_row_line = ''
            # Loop for each text row (each row is three lines tall)
            for inner_index, item in enumerate(r):
                if item == 'X':
                    fancy_row_line += SINGLE_BAR if line % 2 == 0 \
                        else DOUBLE_BAR

                elif item == 'O':
                    fancy_row_line += DOUBLE_BAR if line % 2 == 0 \
                        else SINGLE_BAR

                else:
                    if line % 2 == 0:
                        fancy_row_line += NUMBER.format(number * len(r) + inner_index + 1)
                    else:
                        fancy_row_line += EMPTY

            fancy_row_line += '|\n' if line % 3 else '|'
            fancy_row_full.append(fancy_row_line)

        return fancy_row_full

    for index, row in enumerate(bs):
        fancy_board.append(make_row(index, row))
        if index + 1 != len(bs):
            fancy_board[index].append(SPACER)
    return fancy_board


def add_win_line(bs:list, line_location:dict)->list:
    board_list = make_board(bs)

    match line_location['type']:
        case 'horizontal':
            line_to_change = board_list[line_location['line']][1]
            board_list[line_location['line']][1] =  (
                ''.join([WIN_LINE if char in ' \u2588' else char for char in line_to_change]))
        case 'vertical':
            for row in range(3):
                for index,line in enumerate(board_list[row]):
                    if index != 3:
                        match line_location['line']:
                            case 0:
                                board_list[row][index] = (line[:4] + WIN_LINE +
                                                          line[5:])
                            case 1:
                                board_list[row][index] = (line[:12] + WIN_LINE +
                                                          line[13:])
                            case 2:
                                board_list[row][index] = (line[:20] + WIN_LINE +
                                                          line[21:])
        case 'diagonal':
            chars_placed = 1

            if line_location['line'] == 0:
                for row in range(3):  # Iterate over rows
                    for index, line in enumerate(board_list[row]):
                        if index != 3:
                            replace_pos = chars_placed + 1
                            board_list[row][index] = line[:replace_pos] + WIN_LINE + line[replace_pos + 1:]

                        chars_placed += 2
            elif line_location['line'] == 1:
                chars_placed = 2

                for row in range(3):
                    for index, line in enumerate(board_list[row]):
                        if index < 2:
                            # For this diagonal, positions go backward across rows
                            replace_pos = len(line) - chars_placed - 2
                            board_list[row][index] = line[:replace_pos] + WIN_LINE + line[replace_pos + 1:]
                        elif index == 2:
                            replace_pos = len(line) - chars_placed - 1
                            board_list[row][index] = line[:replace_pos] + WIN_LINE + line[replace_pos + 1:]
                        chars_placed += 2

    return board_list


# Thinking
def find_winner(bs:list)->dict:
    to_check = ['X', 'O']

    for check in to_check:
        # find row
        for index in range(3):
            if all([item == check for item in bs[index]]):
                return {'win':True,'winner': check, 'line_location':{'type':'horizontal', 'line':index, 'winner':check}}
            # find column
            elif all([sub_list[index] == check for sub_list in bs]):
                return {'win':True,'winner': check, 'line_location': {'type': 'vertical', 'line': index, 'winner':check}}
        # diagonals
        if bs[0][0] == bs[1][1] == bs[2][2] == check:
            return {'win':True,'winner': check, 'line_location': {'type': 'diagonal', 'line': 0, 'winner':check}}
        elif bs[0][2] == bs[1][1] == bs[2][0] == check:
            return {'win':True,'winner': check, 'line_location': {'type': 'diagonal', 'line': 1, 'winner':check}}
    if all([item in 'XO' for sublist in bs for item in sublist]):
        return {'win':True,'winner': None}
    return {'win':False, 'winner':None}


def get_options(bs:list)->list:
    return [index for index, _
               in enumerate([item for sublist in bs for item in sublist])
               if is_valid_choice(bs, index)]


def join_or(values:list, sep_one:str = ', ', sep_two:str = 'or')->str:
    count = len(values)
    match count:
        case 0:
            return ''
        case 1:
            return str(values[0])
        case 2:
            return ' '.join([str(values[0]), sep_two, str(values[1])])
        case _ if count > 2 :
               return sep_one.join(str(val) if idx != len(values) - 1
                                    else ' '.join([sep_two, str(val)])
                                    for idx, val in enumerate(values))


def run_game():
    running = True
    game_count = 1
    score = [0,0]
    winner = None
    bots = [easy, medium, hard]


    def set_difficulty():
        say('Please choose a difficulty:')
        bot = ask('1: Easy \n==> 2: Medium \n==> 3: Hard\n')
        while bot not in ['1', '2', '3']:
            say(f'Please choose either: {join_or([1, 2, 3], ", ", "or")}')
            bot = ask('')
        return bots[int(bot) - 1]


    os.system('clear')
    say('Welcome to Tic-Tac-Toe!')
    bot = set_difficulty()

    while running:
        has_won = {'win':False, 'winner':None}

        board_state = initialize_board()

        while not has_won['win']:
            os.system('clear')
            print(f"Difficulty: {bot.__name__}")
            print(f'Round: {str(game_count)}')
            print(f'Score: {score[0]} to {score[1]} (best of 5)')
            print_board(board_state)
            for turn in [get_square, bot]:
                board_state = turn(board_state)
                has_won = find_winner(board_state)
                if has_won['win']:
                    if has_won['winner'] == 'X':
                        os.system('clear')
                        print_with_win_line(board_state, has_won['line_location'])
                        say('You Win the Round!')
                        score[0] += 1
                        break
                    elif has_won['winner'] == 'O':
                        os.system('clear')
                        print_with_win_line(board_state, has_won['line_location'])
                        say('You Lose the Round!')
                        score[1] += 1
                        break
                    else:
                        os.system('clear')
                        print_board(board_state)
                        say('It\'s a Tie!')
                        break
                else:
                    print_board(board_state)
        game_count +=1
        if score[0] > 2:
            game_count = 1
            score = [0, 0]
            winner = 'X'
            say('YOU WIN THE MATCH!')
        elif score[1] > 2:
            game_count = 1
            score = [0, 0]
            winner = 'O'
            say('YOU LOSE THE MATCH!')


        answer = ask(f"Next {'Game' if winner else 'Round' }? (Y/N)")
        while answer.lower() not in ['y','n']:
            say('Please Choose Y or N')
            answer = ask(f'Play Again? (Y/N) {"or Change the Difficulty? (D)" if winner else ""}')

        if answer.lower() == 'n':
            running = False
            os.system('clear')
            say('Thanks For Playing!')
        elif answer.lower() == 'd' and winner:
            bot = set_difficulty()



run_game()