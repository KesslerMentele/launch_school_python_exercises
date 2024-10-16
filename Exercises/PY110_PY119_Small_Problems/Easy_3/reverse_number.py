"""
Full Description:
Write a function that takes a positive integer as an argument and returns that
number with its digits reversed.

Input: int
Output: int


Algorithm:
coerce to string, string slice to reverse, coerce to int

"""

def reverse_number(to_reverse:int)->int:
    return int(str(to_reverse)[::-1])


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True