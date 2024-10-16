"""
Write a function that takes one argument, a list of integers, and returns the
average of all the integers in the list, rounded down to the integer component
of the average. The list will never be empty, and the numbers will always be
positive integers.

Inputs: list of integers
Outputs: integer average of list

Rules:
    Explicit:
        The list will never be empty
        The numbers will always be positive
        Round down the average to an integer

Algorithm:
    create a total variable = 0
    for each item in the list
        add item to total
    divide total by len(items)
    coerce total to int
    return total


"""


def average(numbers:list)->int:
    total = 0
    for number in numbers:
        total += number
    total /= len(numbers)
    return int(total)


print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True