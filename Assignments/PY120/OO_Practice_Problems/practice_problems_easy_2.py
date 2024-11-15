def q1():
    class Game:
        def play(self):
            return 'Start the game!'

    class Bingo(Game):
        pass


def q2():
    class Game:
        count = 0
        def __init__(self, name):
            self.name = name
            Game.count += 1

        def play(self):
            return f'Start the {self.name} game!'

    class Bingo(Game):
        def __init__(self,name, player):
            super().__init__(name)
            self.player_name = player

    class Scrabble(Game):
        def __init__(self,name, player1, player2):
            super().__init__(name)
            self.player_name1 = player1
            self.player_name2 = player2

    bingo = Bingo('Bingo', 'Bill')
    print(Game.count)  # 1
    print(bingo.play())  # Start the Bingo game!
    print(bingo.player_name)  # Bill

    scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
    print(Game.count)  # 2
    print(scrabble.play())  # Start the Scrabble game!
    print(scrabble.player_name1)  # Jill
    print(scrabble.player_name2)  # Sill
    print(scrabble.player_name)

def q5():
    class Greeting:
        @classmethod
        def greet(cls, message):
            print(message)

    class Hello(Greeting):
        @classmethod
        def hi(cls):
            cls.greet('Hi')

    class Goodbye(Greeting):
        def bye(self):
            self.greet('Goodbye')

    Hello.hi()

def q6():
    class Cat:
        def __init__(self, type):
            self.type = type

        def __repr__(self):
            return f'I am a {self.type}'

    print(Cat('hairball'))
    # <__main__.Cat object at 0x10695eb10>

