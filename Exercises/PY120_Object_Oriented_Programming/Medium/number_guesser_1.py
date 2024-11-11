from random import randint
from math import log2


class GuessingGame:

    def __init__(self, min_num = 1, max_num = 100):
        if (not isinstance(min_num, int)) or (not isinstance(max_num, int)):
            raise TypeError('bounds must be integers')
        self._min_num = min_num
        self._max_num = max_num
        self._guesses = int(log2(self._max_num - self._min_num + 1)) + 1



    def get_number(self):
        number = input(f"Enter a number between {self._min_num} and {self._max_num}:")
        while True:
            try:
                if self._max_num > int(number) > self._min_num:
                    return int(number)
            except ValueError:
                pass
            number = input(f'Invalid guess. Enter a number between {self._min_num} and {self._max_num}:')


    def play(self):
        number = randint(self._min_num, self._max_num)
        guesses_left = self._guesses
        win = False
        while guesses_left > 0:
            print(f"You have {guesses_left} guesses remaining.")
            guess = self.get_number()

            if int(guess) == number:
                print("That's the number!\n")
                win = True
                guesses_left = 0
            elif int(guess) > number:
                print('Your guess is too high.\n')
            else:
                print("Your guess is too low.\n")
            guesses_left -= 1
        if win:
            print("You won!")
        else:
            print("You have no more guesses. You lost!")

game = GuessingGame(501, 1500)
game.play()
game.play()