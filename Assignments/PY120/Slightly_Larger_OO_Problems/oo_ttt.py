import random
import os
from pprint import pprint


class Game:
    def __init__(self, size = 3):
        self._size = size
        self._board = Board(size)
        self._human = Player('X', 31)
        self._computer = Player('O', 36)
        self._winner = None
        self._scores = [0,0]
        self._starting_player = self._human
        self._players = [self._human, self._computer]

    def _new_game(self):
        self._board = Board(self._size)
        self._winner = None
        self._scores = [0,0]

    def _play_one_game(self):
        self._new_game()
        while self._winner is None:
            if self._starting_player == self._human:
                print(self._print_board())
                self._player_turn()
            else:
                self._comp_turn()
            if self._winner:
                break
            if self._starting_player == self._human:
                self._comp_turn()
            else:
                print(self._print_board())
                self._player_turn()
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
                elif self._winner == self._computer:
                    self._scores[1] += 1
                    print('You lose!')
                else:
                    self._scores[0] += 1
                    print('You win!')

                print(f'Scores: {self._scores[0]} to {self._scores[1]}')
                self._swap_player()
                if any([score == 1 for score in self._scores]):
                    break

            ans = input("Play again?")
            if not ans.casefold().startswith('y'):
                playing = False

        print("Goodbye!")

    def _swap_player(self):
        if self._starting_player == self._human:
            self._starting_player = self._computer
        else:
            self._starting_player = self._human


    def _comp_turn(self):
        almost = self._board.is_almost_winner()
        moves = self._board.valid_moves()
        if almost[1] is not None and almost[1] != self._computer.marker:
            val = list(almost[0].intersection(set(moves)))[0]
        elif almost[1] is not None and almost[1] == self._computer.marker:
            val = list(almost[0].intersection(set(moves)))[0]
        elif ((self._size ** 2) // 2) + 1 in self._board.valid_moves():
            val = ((self._size ** 2) // 2) + 1
        else:
            val = random.choice(self._board.valid_moves())
        self._board.change_square(val, self._computer.marker)


        if self._board.is_winner()[0]:
            self._winner = self._computer
        elif self._board.is_tie():
            self._winner = "Tie"


    def _player_turn(self):
        val = 0
        move = None
        while True:
            choice = input(
                f"You are: {'X' if self._starting_player == self._human else 'O'}\n"
                f"Choose a square: "
            )
            try:
                if int(choice) in self._board.valid_moves():
                    val = int(choice)
                    move = self._human.marker
                    break
            except ValueError:
                pass
            print("That is not a valid move.")
        self._board.change_square(val, move)
        if self._board.is_winner()[0]:
            self._winner = self._human
        elif self._board.is_tie():
            self._winner = "Tie"

    def _print_board(self):
        board_str = self._board.__repr__()
        for player in self._players:
            board_str = board_str.replace(player.marker, player.colored_marker)
        print(board_str)

    @staticmethod
    def join_or(enum:list, sep:str=', ', end_sep:str=', or ',):
        return sep.join([str(item) for item in enum[:-1]]) + end_sep + str(enum[-1])


class Board:
    LCAP = "*----"
    MCAP = "----*----"
    RCAP = "----*\n"
    LBLANK = "|    "
    MBLANK = "    |    "
    RBLANK = "    |\n"

    TYPES = ['X', 'O', None]

    def __init__(self, size):
        if size % 2 == 0:
            raise ValueError('Size must be an odd number!')
        self._size = size
        self._board = {key: None for key in range(1, (size ** 2) + 1)}

    def __repr__(self):
        largest_number = len(str(self._size ** 2))

        full_line_cap = self.LCAP + ("-" * largest_number) + (
                    (self.MCAP + ("-" * largest_number)) * (self._size - 1)
        ) + self.RCAP

        full_line_blank = self.LBLANK + (" " * largest_number) + (
                    (self.MBLANK + (" " * largest_number)) * (self._size - 1)
        ) + self.RBLANK

        full_line_number = self.LBLANK + '{}' + (
                    (self.MBLANK + '{}') * (self._size - 1)) + self.RBLANK

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
            if all([val == 'X' for val in line.values()]):
                return True, 'X'
            elif all([val == 'Y' for val in line.values()]):
                return True, 'Y'
        return False, None

    def change_square(self, val, mark):
        self._board[val] = mark

    def is_almost_winner(self):
        for line in self.winning_lines:
            if (list(line.values()).count('X') == self._size - 1 and
                    list(line.values()).count(None) == 1):
                return set(line), 'X'
            if (list(line.values()).count('O') == self._size - 1 and
                    list(line.values()).count(None) == 1):
                return set(line), 'O'
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

game = Game(5)
game.play()
