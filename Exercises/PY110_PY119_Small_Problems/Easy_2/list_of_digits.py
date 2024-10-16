"""
Full Description:
Write a function that takes one argument, a positive integer, and returns a
list of the digits in the number.

Input: one positive integer
Output: list of digits


Algorithm:
    coerce to string,
    split to list, coerce items to ints


"""

def digit_list(number:int)->list:
    return [int(item) for item in str(number)]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True