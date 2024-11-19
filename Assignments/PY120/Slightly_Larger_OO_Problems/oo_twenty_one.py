
class Card:
    RANKS = {}
    SUITS = {}

    def __init__(self, rank, suit):
        self.hidden = True
        self._rank = rank
        self._suit = suit

    def flip(self):
        self.hidden = not self.hidden

    pass


class Hand:
    def __init__(self):
        self._cards = []

    def add(self, card:Card):
        pass

    def flip(self):
        for card in self._cards:
            card.flip()


    @property
    def value(self):
        pass



class Participant:
    def __init__(self):
        self._hand = Hand()

    def hit(self):
        pass

    def stay(self):
        pass

    @property
    def is_bust(self):
        pass

    @property
    def score(self):
        return self._hand.value

class Deck:
    def deal(self, hand:Hand):
    pass



class Player(Participant):
    pass

class Dealer(Participant):
    pass

class Game:
    def __init__(self):
        self._player = Player()
        self._dealer = Dealer()
        self._deck = Deck()

    def start(self):
        self._show_welcome_message()
        # deal two to both
        # show dealer and player cards
        # player turn until stay
        # dealer turn
        # show result
        self._show_goodbye_message()

    def _initial_deal(self):
        self._player.hit()
        self._player.hit()
        self._dealer.hit()
        self._dealer.hit()


    @staticmethod
    def _show_welcome_message():
        print('Welcome to Twenty-One!')

    @staticmethod
    def _show_goodbye_message():
        print("Goodbye!")


    pass

