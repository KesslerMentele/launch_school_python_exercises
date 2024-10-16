"""
Full Description:
Write a function that takes a list of positive integers as input, multiplies
all of the integers together, divides the result by the number of entries in
the list, and returns the result as a string with the value rounded to three
decimal places.

Input: list of positive integers
Output: String

rules:
    Explicit:
        - answer must be rounded to three decimal places

Algorithm:
    create a product variable = 1
    for each item in the list multiply the product by the item
    divide the product by the len of the input list
    round it to three decimals // use string formatting to force three decimal places
    return it as a string

"""

def multiplicative_average(multipliers:list)->str:
    product = 1
    for item in multipliers:
        product *= item
    product /= len(multipliers)
    return f"{product:.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
