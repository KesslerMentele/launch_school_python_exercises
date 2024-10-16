"""
Full Description:
Write a function that takes a string argument consisting of a first name, a
space, and a last name. The function should return a new string consisting of
the last name, a comma, a space, and the first name.

Input: string
Output: new string

Rules:
    Explicit:
        The input will be two words separated by a space
        The output must be those words in opposite order with a ', ' between

Algorithm:
    split
    reverse
    join on ', '

"""


def swap_name(input_string:str)->str:
    reordered = input_string.split()
    reordered.reverse()
    return ', '.join(reordered)


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True