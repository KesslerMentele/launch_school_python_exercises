import random


class Move:
    def __init__(self):
        pass


class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        move = None


class Human(Player):
    def choose(self):

        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = choice

class Computer(Player):


    def choose(self):
        self.move = random.choice(Player.CHOICES)


class RPSGame:

    @staticmethod
    def display_welcome_message():
        print('Welcome to Rock, Paper, Scissors!')

    @staticmethod
    def display_goodbye_message():
        print('Thanks for playing! Goodbye!')

    def __init__(self):
        self._player = Human()
        self._computer = Computer()

    def play(self):
        self.display_welcome_message()
        while True:
            self._choose_move(self._player)
            self._choose_move(self._computer)
            self._display_winner()
            if not self._play_again():
                break
        self.display_goodbye_message()

    @staticmethod
    def _choose_move(player:Player | Computer):
        player.choose()
        pass

    def _human_wins(self):
        p_move = self._player.move
        c_move = self._computer.move
        if ((p_move == 'rock' and c_move == 'scissors') or
                (p_move == 'paper' and c_move == 'rock') or
                (p_move == 'scissors' and c_move == 'paper')):
            return True
        return False

    def _computer_wins(self):
        p_move = self._player.move
        c_move = self._computer.move
        if ((c_move == 'rock' and p_move == 'scissors') or
              (c_move == 'paper' and p_move == 'rock') or
              (c_move == 'scissors' and p_move == 'paper')):
            return True
        return False


    def _display_winner(self):
        p_move = self._player.move
        c_move = self._computer.move

        print(f'You chose: {p_move}')
        print(f'The computer chose: {c_move}')


        if self._human_wins():
            print('You win!')
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print("It's a tie")

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

    def compare(self, move1:Move, move2:Move):
        pass

game = RPSGame()
game.play()