"""
Egyptian fraction:
The sum of a series of distinct unit fractions.

Every positive rational number cna be represented as a unit fraction

Function One:
    egyptian:
        Input: A fraction representing a rational number
        Output: a list of integers representing the denominators of the egyptian fraction for that number
    unegyptian:
        Input: A list of integers
        Output: the sum returned by that list of denominators

"""

from fractions import Fraction


def egyptian(input_num:Fraction)->list:
    denominators = []
    current_denom = 1
    while input_num != 0:
        if input_num - (Fraction(1,current_denom)) >= 0:
            input_num -= (Fraction(1,current_denom))
            denominators.append(current_denom)
        current_denom +=1
    return denominators


def unegyptian(denominators:list)->int:
    return sum([Fraction(1,denominator) for denominator in denominators])



print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))
