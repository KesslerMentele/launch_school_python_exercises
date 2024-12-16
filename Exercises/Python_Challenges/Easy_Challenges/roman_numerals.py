#
#
# Roman numerals:
#   I = 1
#   V = 5
#   X = 10
#   L = 50
#   C = 100
#   D = 500
#   M = 1000
#
# intdiv 1000, put that many Ms
# intdiv 100,
#   if >5 put number - 5 Cs then a D
#   if 5 put a D
#   if 4 put a D then a C
#   if <4 put number of Cs
# intdiv 10,
#   if >5 put number - 5 Xs then an L
#         #   if 5 put an L
#         #   if 4 put an L then an X
#         #   if <4 put number of Xs

class RomanNumeral:


    def __init__(self, value):
        self.value = value

    @staticmethod
    def _roman_weirdness(val, numeral_place):
        NUMERALS = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

        if val == 9:
            return NUMERALS[numeral_place - 1] + NUMERALS[numeral_place + 1]
        elif val > 5:
            return NUMERALS[numeral_place] + (NUMERALS[numeral_place - 1] * (val - 5))
        elif val == 5:
            return NUMERALS[numeral_place]
        elif val == 4:
            return NUMERALS[numeral_place - 1] + NUMERALS[numeral_place]
        elif val < 4:
            return NUMERALS[numeral_place - 1] * val


    def to_roman(self)->str:

        roman = ''

        roman += 'M' * (self.value // 1000 ) % 10
        roman += self._roman_weirdness((self.value // 100) % 10, 5)
        roman += self._roman_weirdness((self.value // 10) % 10, 3)
        roman += self._roman_weirdness(self.value  % 10, 1)
        return roman

