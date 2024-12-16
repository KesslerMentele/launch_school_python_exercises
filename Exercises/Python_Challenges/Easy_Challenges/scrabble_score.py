


class Scrabble:
    LETTER_VALUES = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1,
        "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    def __init__(self, word):
        self._word = word

    def score(self):
        return self.__class__.calculate_score(self._word)

    @classmethod
    def calculate_score(cls, word)->int:
        val = 0
        if not word:
            return 0
        word = ''.join(word.split())
        for char in word:
            val += cls.LETTER_VALUES[char.upper()]
        return val
    pass