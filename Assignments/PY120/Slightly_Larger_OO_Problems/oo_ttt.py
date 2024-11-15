# Classes: Game, Board, Square, Marker, Row, Player, Human, Computer
# Verbs: Play, Mark, Move, Place
#
#
#
#
#
#
#
#
import random


class Game:
    def __init__(self):
        self._board = Board()
        self._human = Human()
        self._computer = Computer()
        self._winner = None

    def play(self):
        print('Welcome to Tic-Tac-Toe!')
        while self._winner is None:
            self._turn(self._human)
            if self._winner:
                break
            self._turn(self._computer)
        if self._winner == "Tie":
            print('It\'s a Tie!')
        elif self._winner == self._computer:
            print('You lose!')
        else:
            print('You win!')
        print("Goodbye!")


    def _turn(self, player):
        print(self._board)
        (val,move) = player.take_turn()
        self._board.change_square(val,move)
        if self._board.is_winner():
            self._winner = player
        elif self._board.is_tie():
            self._winner = "Tie"

class Square:
    TYPES = ['X','O', None]
    def __init__(self, mtype = None):
        if mtype not in Square.TYPES:
            raise ValueError('not a valid marker type')
        self._type = mtype

    def __repr__(self):
        return self._type if self._type else ' '

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, val):
        if val not in Square.TYPES:
            raise ValueError('Not a valid square type')
        self._type = val



class Board:
    def __init__(self):
        self._squares = {key:Square() for key in range(1,10)}

    def __repr__(self):
        return (f"*-----*-----*-----*\n"
                f"|  {self._squares[1]}  |  {self._squares[2]}  |  {self._squares[3]}  |\n"
                f"*-----*-----*-----*\n"
                f"|  {self._squares[4]}  |  {self._squares[5]}  |  {self._squares[6]}  |\n"
                f"*-----*-----*-----*\n"
                f"|  {self._squares[7]}  |  {self._squares[8]}  |  {self._squares[9]}  |\n"
                f"*-----*-----*-----*\n")

    def change_square(self, val, mark):
        self._squares[val].type = mark

    def is_winner(self):
        wins = [[1,2,3], [4,5,6],
                [7,8,9], [1,4,7],
                [2,5,8], [3,6,9],
                [1,5,9], [3,5,7]]
        for line in wins:
            if self._squares[line[0]].type is not None:
                if all([self._squares[line[0]].type == self._squares[idx].type
                    for idx in line]):
                    return True
        return False

    def is_tie(self):
        if all(sq.type is not None for sq in self._squares.values()):
            return True



class Player:
    def __init__(self, marker = 'Empty'):
        self.marker = marker

    def take_turn(self):
        pass



class Human(Player):
    def __init__(self):
        super().__init__('X')

    def take_turn(self):
        val = input()
        return int(val), self.marker

class Computer(Player):
    def __init__(self):
        super().__init__('O')

    def take_turn(self):
        val = random.choice(range(1,10))
        return int(val), self.marker
game = Game()
game.play()