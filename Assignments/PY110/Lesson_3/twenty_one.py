import os
import random


class Card:
    suits = {
        "Spades": 0x1F0A0,
        "Hearts": 0x1F0B0,
        "Diamonds": 0x1F0C0,
        "Clubs": 0x1F0D0
    }

    ranks = {
        "Ace": 0x1,
        "Two": 0x2,
        'Three': 0x3,
        'Four': 0x4,
        'Five': 0x5,
        'Six': 0x6,
        'Seven': 0x7,
        'Eight': 0x8,
        'Nine': 0x9,
        'Ten': 0xA,
        "Jack": 0xB,
        "Queen": 0xD,
        "King": 0xE
    }

    faces = ['King', 'Queen', 'Jack']


    def __init__(self, rank, suit):
        if rank not in self.ranks:
            raise ValueError(f"Invalid rank value: {rank}. "
                             f"Must be one of {list(self.ranks.keys())}")
        if suit not in self.suits:
            raise ValueError(f"Invalid suit value: {suit}. "
                             f"Must be one of {list(self.suits.keys())}")

        self.rank = rank
        self.suit = suit

        self.is_face = False
        self.is_ace = False
        self.is_number = False

        if self.is_face:
            self.value = 10
        self.value = self.ranks[self.rank]

        if rank in self.faces:
            self.is_face = True
        elif rank == "Ace":
            self.is_ace = True
            self.is_number = True
        else:
            self.is_number = True


    def __repr__(self):
        return (f'\033[{"31" if self.color() == 'red' else "0"}m'
                f'{self.rank} of {self.suit}\033[0m')


    def __eq__(self, other):
        if isinstance(other, str):
            other = other.lower()
            return (self.rank.lower() == other
                    or self.suit.lower() == other.lower()
                    or str(self.value).lower() == other.lower()
                    or self.color().lower() == other.lower())
        return False

    def __str__(self):
        return (f'\033[{"31" if self.color() == 'red' else "0"}m'
                f'{self.rank} of {self.suit}\033[0m')

    def __int__(self):
        return self.value



    def color(self):
        return 'red' if self.suit in ['Hearts', 'Diamonds'] else 'black'


    @staticmethod
    def show_back():
        return "\U0001F0A0"


    def show_char(self):
        return (f'\033[{"31" if self.color() == 'red' else "0"}m'
                f'{chr(self.suits[self.suit] + self.ranks[self.rank])}\033[0m')


RANKS = [
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'King',
    'Queen',
    'Ace'
]
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
STARTING_HAND_SIZE = 2
deck = [Card(rank, suit) for suit in SUITS for rank in RANKS ]

def say(msg):
    print(f'==>{msg}')


def ask(question:str)->str:
    return input(f'==> {question}')


def shuffle():
    random.shuffle(deck)


def deal(card_to:list, card_from:list, count:int = 1):
    for _ in range(count):
        card = card_from.pop()
        card_to.append(card)


def value_of(hand:list)->int:
    value = sum([int(card) if int(card) < 10 else 10 for card in hand])
    if any([card.is_ace for card in hand]) and value + 10 <= 21:
        value += 10
    return value

def is_busted(hand:list)->bool:
    return value_of(hand) > 21

def show_hand(hand:list, hide_one:bool = False):
    if not hide_one:
        print(', '.join([str(card) for card in hand]))

        say(f'Value: {value_of(hand)}')
    else:
        print(', '.join([*[str(card) for card in hand[:-1]],
                         Card.show_back()]))
        say(f'Value (of face up): {value_of(hand[:-1])}')


def take_turn(card_to:list, card_from:list, is_dealer:bool = False):
    choices = ['hit', 'stay']

    choice = ''
    while not is_busted(card_to):
        if not is_dealer:
            say('Hit or Stay?')
            choice = ask('')
            while choice.lower() not in choices:
                say('Please Choose Either Hit or Stay')
                choice = ask('')
            if choice.lower() == 'hit':
                deal(card_to, card_from)
                show_info()
            else:
                return {'bust':False}

        else:
            while value_of(card_to) <= 17:
                deal(card_to, card_from)
                show_info()
            if not is_busted(card_to):
                return {'bust': False}
    return {'bust':True}

def show_info(hide_dealer = True):
    os.system('clear')
    print('Dealer\'s Hand')
    show_hand(dealer, hide_one=hide_dealer)
    print('\n\n')
    print('Your Hand:')
    show_hand(player)
    print('\n\n')


while True:
    shuffle()
    dealer = []
    player = []
    deal(player, deck, count=2)
    deal(dealer,deck,count=2)
    show_info()
    result = take_turn(player, deck)
    if result['bust']:
        say('You Busted! Dealer Wins!')
    else:
        result = take_turn(dealer, deck, is_dealer=True)
        show_info(hide_dealer=False)
        if result['bust']:
            say('Dealer Busted! You Win!')
    if not result['bust']:
        if value_of(player) > value_of(dealer):
            say("You Win!")
        elif value_of(dealer) > value_of(player):
            say('You Lose!')
        else:
            say('It\'s a Tie!')
    again = ask('Play Again! (Y/N)')
    while again.lower() not in ['y','n']:
        say('Please choose Yes or No (Y or N)')
        again = ask('')
    if again.lower() == 'n':
        break
