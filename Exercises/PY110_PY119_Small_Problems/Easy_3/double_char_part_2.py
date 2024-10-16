"""
Full Description:
Write a function that takes a string, doubles every consonant in the string,
and returns the result as a new string. The function should not double vowels
('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

Input: string
Output: string

Rules:
    Explicit:
        Double every consonant in the string
        Only ASCII Characters

Algorithm:
    join array of chars from input where char if not consonant else char * 2

"""


def is_consonant(char: str) -> bool:
    if not is_vowel(char) and char.isalpha():
        return True
    return False


def is_vowel(char: str) -> bool:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True


def double_consonants(to_repeat:str)->str:
    return ''.join([char if not is_consonant(char) else char * 2 for char in to_repeat])

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")