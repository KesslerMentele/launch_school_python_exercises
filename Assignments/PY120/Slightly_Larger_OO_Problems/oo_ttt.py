import random
import os
from pprint import pprint


class Game:

    PLAYER_VALUES = (
        ('X', 31),
        ('O', 32),
        ('Y', 34),
        ('Z', 36),
        ('A', 95),
        ('B', 93),
    )

    def __init__(self,h_count = 1, c_count = 1, size = 3):
        if (h_count + c_count) > 6:
            raise ValueError('there can only be up to 6 players')
        self._size = size
        self._humans = [Player(*Game.PLAYER_VALUES[idx]) for idx in range(h_count)]
        self._computers = [Player(*Game.PLAYER_VALUES[idx]) for idx in range(h_count, c_count+h_count)]
        self._winner = None
        self._scores = [0,0]
        self._board = Board(size, [player.marker for player in self._players])


    def _new_game(self):
        self._board = Board(self._size, [player.marker for player in self._players])
        self._winner = None
        self._scores = [0,0]

    def _play_one_game(self):
        self._new_game()
        while True:
            for idx, player in enumerate(self._players):
                if player in self._humans:
                    self._print_board()
                    self._player_turn(idx)
                    os.system('clear')
                else:
                    self._comp_turn(idx)
                if self._winner:
                    break
            if self._winner:
                break
        os.system('clear')


    def play(self):
        print('Welcome to Tic-Tac-Toe!')
        playing = True
        while playing:
            while True:
                self._play_one_game()
                print(self._print_board())
                if self._winner == "Tie":
                    print('It\'s a Tie!')
                elif self._winner in self._computers:
                    self._scores[1] += 1
                    print(f'Computer {self._winner.colored_marker} wins!')
                elif self._winner in self._players:
                    self._scores[0] += 1
                    print(f'Player {self._winner.colored_marker} wins!')

                print(f'Scores: {self._scores[0]} to {self._scores[1]}')
                if any([score == 1 for score in self._scores]):
                    break

            ans = input("Play again?")
            if not ans.casefold().startswith('y'):
                playing = False

        print("Goodbye!")


    def _comp_turn(self, num):
        comp = self._players[num]
        almost = self._board.is_almost_winner()
        moves = self._board.valid_moves()
        if almost[1] is not None and almost[1] != comp.marker:
            val = list(almost[0].intersection(set(moves)))[0]
        elif almost[1] is not None and almost[1] == comp.marker:
            val = list(almost[0].intersection(set(moves)))[0]
        elif ((self._size ** 2) // 2) + 1 in self._board.valid_moves():
            val = ((self._size ** 2) // 2) + 1
        else:
            val = random.choice(self._board.valid_moves())
        self._board.change_square(val, comp.marker)


        if self._board.is_winner()[0]:
            self._winner = comp
        elif self._board.is_tie():
            self._winner = "Tie"

    def _player_turn(self, num):
        val = 0
        move = None
        player = self._players[num]
        while True:
            choice = input(
                f"You are: {player.marker}\n"
                f"Choose a square: "
            )
            try:
                if int(choice) in self._board.valid_moves():
                    val = int(choice)
                    move = player.marker
                    break
            except ValueError:
                pass
            print("That is not a valid move.")
        self._board.change_square(val, move)
        if self._board.is_winner()[0]:
            self._winner = player
        elif self._board.is_tie():
            self._winner = "Tie"

    def _print_board(self):
        board_str = self._board.__repr__()
        for player in self._players:
            board_str = board_str.replace(player.marker, player.colored_marker)
        print(board_str)

    @property
    def _players(self):
        humans = self._humans
        comps = self._computers
        every_other = [player for pair in zip(humans, comps) for player in pair]
        every_other.extend(humans[len(comps):] if len(humans) > len(comps) else comps[len(humans):])
        return every_other

    @property
    def _player_count(self):
        return len(self._humans) + len(self._computers)

    @staticmethod
    def join_or(enum:list, sep:str=', ', end_sep:str=', or ',):
        return sep.join([str(item) for item in enum[:-1]]) + end_sep + str(enum[-1])


class Board:

    def __init__(self, size, markers):
        if size % 2 == 0:
            raise ValueError('Size must be an odd number!')
        self._markers = markers
        self._size = size
        self._board = {key: None for key in range(1, (size ** 2) + 1)}

    def __repr__(self):
        LCAP = "*----"
        MCAP = "----*----"
        RCAP = "----*\n"
        LBLANK = "|    "
        MBLANK = "    |    "
        RBLANK = "    |\n"
        largest_number = len(str(self._size ** 2))

        full_line_cap = LCAP + ("-" * largest_number) + (
                    (MCAP + ("-" * largest_number)) * (self._size - 1)
        ) + RCAP

        full_line_blank = LBLANK + (" " * largest_number) + (
                    (MBLANK + (" " * largest_number)) * (self._size - 1)
        ) + RBLANK

        full_line_number = LBLANK + '{}' + (
                    (MBLANK + '{}') * (self._size - 1)) + RBLANK

        full_board = full_line_cap
        for i in range(len(self._rows)):
            full_board += (full_line_blank + full_line_number +
                           full_line_blank + full_line_cap)
        board_cells = full_board.format(*[
            str(self._board[key]
                if self._board[key] is not None
                else key).rjust(largest_number, ' ')
            for key in range(1, (self._size ** 2) + 1)
        ])
        return board_cells

    @property
    def _rows(self):
        rows = []
        for r in range(self._size):
            row = {idx: self._board[idx] for idx in range(
                r * self._size + 1,
                (r + 1) * self._size + 1
            )}
            rows.append(row)
        return rows

    @property
    def _cols(self):
        cols = []
        for c in range(1, self._size + 1):
            col = {idx: self._board[idx] for idx in
                   range(c, (self._size - 1) * self._size + c + 1, self._size)}
            cols.append(col)
        return cols

    @property
    def _diags(self):
        rows = list(self._rows)
        diag1 = {list(row.keys())[idx]: list(row.values())[idx]
                 for idx, row in enumerate(rows)}
        diag2 = {
            list(row.keys())[-(idx + 1)]: list(row.values())[-(idx + 1)]
            for idx, row in enumerate(rows)}
        return [diag1, diag2]

    @property
    def winning_lines(self):
        return self._rows + self._cols + self._diags

    def get_board_vals(self, line: list):
        return [val for key, val in self._board if key in line]

    def is_winner(self):
        for line in self.winning_lines:
            for marker in self._markers:
                if all([val == marker for val in line.values()]):
                    return True, marker
        return False, None

    def change_square(self, val, mark):
        self._board[val] = mark

    def is_almost_winner(self):
        for line in self.winning_lines:
            for marker in self._markers:
                if (list(line.values()).count(marker) == self._size - 1 and
                        list(line.values()).count(None) == 1):
                    return set(line), marker

        return None, None

    def is_tie(self):
        if all(sq is not None for sq in self._board.values()):
            return True
        return False


    def valid_moves(self):
        return [key for key, square
                in self._board.items()
                if square is None]


class Player:
    def __init__(self, marker='Empty', color=37):
        self.marker = marker
        self.colored_marker = f'\033[1;{color}m{marker}\033[0m'

# The Game function takes three arguments, number of human players,
# number of computer players, and an odd number board size.
# The game can be played with a total of up to six players,
# either humans or computers
# It can be played with 0-6 humans and 0-6 computers, it doesn't care
#

game = Game(0,6,15)
game.play()
