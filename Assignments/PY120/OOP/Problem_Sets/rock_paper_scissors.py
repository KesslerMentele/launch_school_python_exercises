import random


class Move:
    TYPES = ('rock', 'paper', 'scissors', 'spock', 'lizard')


    @staticmethod
    def get_winner(move1, move2):
        index1 = Move.TYPES.index(move1) + 1
        index2 = Move.TYPES.index(move2) + 1
        print(index1)
        print(index2)
        if index2 > index1:
            return move2 if (index2 - index1) % 2 != 0 else move1
        return move1 if (index1 - index2) % 2 != 0 else move2

    @staticmethod
    def get_list():
        return ', '.join(Move.TYPES)

    def __init__(self):
        self._choice = Move.TYPES[0]

    def __str__(self):
        return self._choice

    def __repr__(self):
        return self.__str__()

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, val):
        if val not in Move.TYPES:
            raise ValueError('Not a Valid Move')

        self._choice = val





class Player:

    def __init__(self):
        self.move = Move()
        self._score = 0

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, val):
        if isinstance(val, int):
            self._score = val
        else:
            raise TypeError('Score must be an integer')



class Human(Player):


    def __init__(self):
        super().__init__()

    def choose(self):

        prompt = f'Please choose {Move.get_list()}: '

        while True:
            choice = input(prompt).lower()
            if choice in Move.TYPES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move.choice = choice

class Computer(Player):

    def __init__(self):
        super().__init__()


    def choose(self):
        self.move.choice = random.choice(Move.TYPES)


class RPSGame:

    @staticmethod
    def display_welcome_message():
        print(f'Welcome to {Move.get_list()}!')

    @staticmethod
    def display_goodbye_message():
        print('Thanks for playing! Goodbye!')

    @staticmethod
    def _play_again():
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

    @staticmethod
    def _choose_move(player: Player | Computer):
        player.choose()

    def __init__(self):
        self._player = Human()
        self._computer = Computer()
        self._best_of = None

    def _players(self):
        return self._player, self._computer

    def play(self, best_of:int = 5):
        self.display_welcome_message()
        self._best_of = best_of
        while True:
            while not any([competitor.score > (self._best_of // 2)
                           for competitor in self._players()]):
                self._show_scores()
                self._choose_move(self._player)
                self._choose_move(self._computer)
                self._round_winner()
            self._game_winner()
            if not self._play_again():
                break
        self.display_goodbye_message()


    def _show_scores(self):
        print(f'The Scores are:\nYou: {self._player.score}     '
              f'Computer: {self._computer.score}')


    def _round_winner(self):
        p_move = self._player.move.choice
        c_move = self._computer.move.choice

        print(f'You chose: {p_move}')
        print(f'The computer chose: {c_move}')

        if p_move == c_move:
            print('It\'s a Tie!')
        elif Move.get_winner(p_move, c_move) == p_move:
            self._player.score += 1
            print('You Win the round!\n')
        else:
            self._computer.score += 1
            print('Computer Wins the round!\n')

    def _game_winner(self):
        if self._player.score > (self._best_of // 2):
            print("You Win the Game!")
        else:
            print("You Lose the Game!")


game = RPSGame()
game.play()
