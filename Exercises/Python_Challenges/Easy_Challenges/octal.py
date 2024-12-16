# Input: string of numbers in Octal
# Output: number in decimal

class Octal:
    def __init__(self, octal:str):
        self.octal = octal
    def to_decimal(self):
        if not self.octal.isnumeric() or any([int(digit) > 7 for digit in self.octal]):
            return 0

        values = []
        for idx, digit in enumerate(self.octal[::-1]):
            values.append(int(digit) * (8**idx))
        return sum(values)
