import random




class Card:
    suits = {
        "Spades": 0x1F0A0,
        "Hearts": 0x1F0B0,
        "Diamonds": 0x1F0C0,
        "Clubs": 0x1F0D0
    }
    faces = {
        "Ace": 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 0xA,
        "Jack": 0xB,
        "Queen": 0xD,
        "King": 0xE
    }

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f'\033[{"31" if self.color() == 'red' else "0"}m{self.face} of {self.suit}\033[0m'

    def value(self):
        if isinstance(self.face, int):
            return self.face
        elif self.face == 'Ace':
            return [1,11]
        else:
            return 10

    def color(self):
        return 'red' if self.suit in ['Hearts', 'Diamonds'] else 'black'

    def show_back(self):
        return "\U0001F0A0"

    def show_char(self):
        return f'\033[{"31" if self.color() == 'red' else "0"}m{chr(self.suits[self.suit] + self.faces[self.face])}\033[0m'


FACES = [1,2,3,4,5,6,7,8,9,10, 'Jack', 'King', 'Queen', 'Ace']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
STARTING_HAND_SIZE = 2
deck = [Card(face, suit) for suit in SUITS for face in FACES ]


def shuffle():
    random.shuffle(deck)

def deal(card_to:list, card_from:list):
    card = card_from.pop()
    card_to.append(card)



shuffle()



