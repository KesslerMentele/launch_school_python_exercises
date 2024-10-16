"""
Full Description:
Write a function that takes a string, doubles every character in the string,
then returns the result as a new string.

Input: string
Output: new string, every character twice




"""

def repeater(to_repeat:str)->str:
    return ''.join([char * 2 for char in to_repeat])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True