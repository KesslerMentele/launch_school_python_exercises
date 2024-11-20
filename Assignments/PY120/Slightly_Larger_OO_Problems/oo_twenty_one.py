import random


class Card:
    RANKS = {
        2:2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
        10:10,
        'Jack':10,
        'Queen':10,
        'King':10,
        "Ace":'Ace'
    }
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')


    def __init__(self, rank, suit):
        self._hidden = True
        if rank not in Card.RANKS.keys():
            raise ValueError('Invalid Rank')
        if suit not in Card.SUITS:
            raise ValueError('Invalid Suit')
        self._rank = rank
        self._suit = suit

    def __str__(self):
        if self._hidden:
            return '\033[1;30;107m Hidden Card \033[0m'
        return f'{self._color()} {self._rank} of {self._suit} \033[0m'

    def flip(self, hidden=None):
        self._hidden = hidden if hidden is not None else not self._hidden

    def hide(self):
        self._hidden = True

    def reveal(self):
        self._hidden = False

    @property
    def hidden(self):
        return self._hidden

    def is_face_card(self):
        return self._rank in ('Jack', 'Queen', 'King')

    def is_ace(self):
        return self._rank == "Ace"

    def _color(self):
        if self._suit in ("Diamonds", "Hearts"):
            return "\033[1;31;107m"
        else:
            return '\033[1;30;107m'

    @property
    def value(self):
        return Card.RANKS[self._rank]



class Hand:
    def __init__(self):
        self._cards = []

    def __str__(self):

        return ', '.join([str(card) for card in self._cards])

    def add(self, card:Card):
        if not isinstance(card, Card):
            raise  TypeError('You can only add cards to your hand')
        self._cards.append(card)

    def flip(self):
        for card in self._cards:
            card.flip()

    def show(self):
        for card in self._cards:
            card.reveal()
        print(self)

    def has_ace(self):
        for card in self._cards:
            if card.is_ace():
                return True
        return False

    @property
    def value(self, include_hidden=False):
        val = 0
        aces = 0
        for card in self._cards:
            if not include_hidden and card.hidden:
                continue
            if isinstance(card.value, int):
                val += card.value
            else:
                aces += 1
        if aces:
            for _ in range(aces):
                if val + 10 > 21:
                    val += 1
                else:
                    val += 10
        return val



class Participant:
    def __init__(self):
        self.hand = Hand()

    def add(self, card:Card):
        self.hand.add(card)

    @property
    def is_bust(self):
        return self.hand.value > 21

    @property
    def score(self):
        return self.hand.value

class Deck:

    def __init__(self):
        self.cards = [
            Card(rank,suit)
            for suit in Card.SUITS
            for rank in Card.RANKS.keys()
        ]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hidden=False):
        card = self.cards.pop()
        card.flip(hidden)
        return card


class TwentyOneGame:
    def __init__(self):
        self._player = Participant()
        self._dealer = Participant()
        self._deck = Deck()
        self._winner = None

    def _new_game(self):
        self._player = Participant()
        self._dealer = Participant()
        self._deck = Deck()
        self._winner = None

    def start(self):
        self._show_welcome_message()
        again = True

        while again:
            self._new_game()
            self._initial_deal()
            self._show()
            self._player_turn()
            print('\n\n')

            if self._winner:
                print("You Busted! You lose!")
            else:
                self._dealer_turn()
                if self._winner:
                    print("Dealer Busted! You Win!")
                else:
                    if self._player.score > self._dealer.score:
                        print('You Win!')
                    elif self._dealer.score > self._player.score:
                        print('You Lose!')
                    else:
                        print('Tie Game!')
            again = False if not input('Play again? (Y/N)').casefold().startswith('y') else True
        self._show_goodbye_message()



    def _initial_deal(self):
        self._player.add(self._deck.deal())
        self._player.add(self._deck.deal())
        self._dealer.add(self._deck.deal(hidden=True))
        self._dealer.add(self._deck.deal())

    def _show(self):
        self._show_dealer_hand()
        print('\n\n')
        self._show_player_hand()


    def _show_player_hand(self):
        print(f'Your Hand (Value {self._player.score}):')
        print(self._player.hand)


    def _show_dealer_hand(self):
        print(f'Dealer\'s Hand (Value {self._dealer.score}):')
        print(self._dealer.hand)


    def _player_turn(self):
        print("What will you do?")
        choice = None
        while choice != 'stay':
            choice = input("'Hit', or 'Stay':").casefold()
            if choice == 'hit':
                self._player.add(self._deck.deal())
                self._show_player_hand()
                if self._player.is_bust:
                    self._winner = self._dealer
                    return

    def _dealer_turn(self):
        while True:
            self._show_dealer_hand()
            if self._dealer.is_bust:
                self._winner = self._player
                return
            if self._dealer.score >=17:
                return
            self._dealer.add(self._deck.deal())

    @staticmethod
    def _show_welcome_message():
        print('Welcome to Twenty-One!')

    @staticmethod
    def _show_goodbye_message():
        print("Goodbye!")


    pass

test = TwentyOneGame()
test.start()


