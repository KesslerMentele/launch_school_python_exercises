"""
The error is raised because of the recursive call to the function sum()
owing to the fact that the user-defined function sum() shadows the built-in
sum(). To fix this error we simply need to rename sum() to something else

:)
"""


something_else = sum

def sum(numbers, factor):
    return factor * something_else(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)

