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


    @property
    def rank(self):
        return self._rank


cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards)  == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True