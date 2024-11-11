from random import randint

class Deck:
    RANKS = {
        'Ace': 14,
        'King': 13,
        'Queen': 12,
        'Jack': 11,
        10: 10,
        9: 9,
        8: 8,
        7: 7,
        6: 6,
        5: 5,
        4: 4,
        3: 3,
        2: 2,
    }
    SUITS = ['Diamonds', 'Hearts', 'Clubs', 'Spades']


    def __init__(self):
        self._cards = []
        self._new_deck()

    def _new_deck(self):
        self._cards = [Card(rank, suit) for rank in Deck.RANKS.keys() for suit
                       in Deck.SUITS]
        self.shuffle()

    def shuffle(self):
        new_order = []
        current_order = self._cards
        while len(current_order) > 0:
            new_order.append(current_order.pop(randint(0,len(current_order) - 1)))
        self._cards = new_order


    def draw(self):
        if len(self._cards) == 0:
            self._new_deck()
        return self._cards.pop(0)

class Card:
    RANKS = {
        'Ace': 14,
        'King': 13,
        'Queen': 12,
        'Jack': 11,
        10: 10,
        9: 9,
        8: 8,
        7: 7,
        6: 6,
        5: 5,
        4: 4,
        3: 3,
        2: 2,
             }
    SUITS = ['Diamonds', 'Hearts', 'Clubs', 'Spades']


    def __init__(self, rank: str | int, suit: str):
        if not (isinstance(rank, str) or isinstance(rank, int) or isinstance(suit, str)):
            raise TypeError('Rank must be either a string or integer, and suit must be an integer')
        try:
            value = int(rank)
            if 15 > value > 0:
                self._rank = next((k for k,v in Card.RANKS.items() if v == value), None)
                self._value = value
            if not self._rank:
                raise ValueError('Rank must be either a string cardname, or a value from 1 to 14')
        except ValueError:
            if rank.capitalize() in Card.RANKS.keys():
                self._rank = rank.capitalize()
                self._value = Card.RANKS[self._rank]

        if suit.capitalize() not in Card.SUITS:
            raise ValueError("Suit must be: Diamonds, Hearts, Clubs, or Spades")
        self._suit = suit.capitalize()


    def __gt__(self, other):
        if not (isinstance(other, Card) or isinstance(other, int)):
            return NotImplemented
        if isinstance(other, Card):
            return self._value > other._value
        return self._value > other


    def __lt__(self, other):
        if not (isinstance(other, Card) or isinstance(other, int)):
            return NotImplemented
        if isinstance(other, Card):
            return self._value < other._value
        return self._value < other


    def __eq__(self, other):
        if not (isinstance(other, Card) or isinstance(other, int)):
            return NotImplemented
        if isinstance(other, Card):
            return self._value == other._value
        return self._value == other


    def __str__(self):
        return f'{self._rank} of {self._suit}'

    def __repr__(self):
        return self.__str__()

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit


deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).