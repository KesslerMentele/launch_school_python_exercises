"""
The list is not changed in the function. Each item is multiplied, but because integers are not mutable, this does not
change the values store in the list.

To fix we use a list comprehension to construct a new list of the multiplied values
"""


def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])