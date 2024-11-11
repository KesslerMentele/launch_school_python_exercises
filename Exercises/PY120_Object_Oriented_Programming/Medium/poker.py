from itertools import filterfalse
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


    def draw(self, count = 1):
        if len(self._cards) == 0:
            self._new_deck()
        drawn = []
        while count > 0:
            drawn.append(self._cards.pop(0))
            count -= 1
        return drawn


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

    @property
    def value(self):
        return self._value

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck:Deck):
        self._hand:list = deck.draw(5)


    def print(self):
        for card in self.hand:
            print(card)


    @property
    def hand(self):
        return self._hand


    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _has_duplicates(self, count:int | list):
        cards = [card for card in self.hand]

        card_values = {}
        for _ in range(len(cards)):
            card = cards.pop()
            if card.rank in card_values.keys():
                card_values[card.rank] += 1
            else:
                card_values[card.rank] = 1
        if isinstance(count, int):
            if count <= 0:
                raise ValueError('Cannot check for zero cards')
            if any([v >= count for v in card_values.values()]):
                return True
            return False
        elif isinstance(count, list):
            count.sort()
            found = len(count)
            if len(count) > 2:
                raise ValueError('Cannot check for more than two counts')
            if sum(count) > len(self.hand):
                raise ValueError('The sum of the counts cannot be greater than the hand size')
            while len(count) > 0:
                length = count.pop()
                for check in range(length, 6):
                    for k, v in card_values.items():
                        if v == check:
                            found -= 1
                            card_values.pop(k)
                            break
            if found == 0:
                return True
            return False


    def _is_royal_flush(self):
        return self._is_straight_flush() and min(self.hand) == 10



    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()



    def _is_four_of_a_kind(self):
        return self._has_duplicates(4)


    def _is_full_house(self):
        return self._has_duplicates([2,3])


    def _is_flush(self):
        return all([item.suit == self.hand[0].suit for item in self.hand])


    def _is_straight(self):
        return all([(min(self.hand).value + count)
                                     in self.hand for count in range(5)])


    def _is_three_of_a_kind(self):
        return self._has_duplicates(3)


    def _is_two_pair(self):
        return self._has_duplicates([2,2])


    def _is_pair(self):
        return self._has_duplicates(2)


class TestDeck(Deck):
    def __init__(self, cards):
        self._cards = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")