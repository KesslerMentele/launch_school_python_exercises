from random import randint


class GuessingGame:
    @staticmethod
    def play():
        number = randint(1,100)
        guesses_left = 7
        win = False
        while guesses_left > 0:
            print(f"You have {guesses_left} remaining.")
            while True:
                guess = input("Enter a number between 1 and 100:")
                try:
                    int(guess)
                except TypeError:
                    print(Invalid guess. Enter a number between 1 and 100:)

            if int(guess) == number:
                print("That's the number!")
                win = True
                break
            elif int(guess) > number:
                print('Your guess is too high.')
            else:
                print("Your guess is too low.")
        if win:
            print("You won!")
        else:
            print("You have no more guesses. You lost!")

game = GuessingGame()
game.play()
game.play()