"""
Full Description:
Write a function that takes a string as an argument and returns True if all
parentheses in the string are properly balanced, False otherwise. To be
properly balanced, parentheses must occur in matching '(' and ')' pairs.

Input: string
Output: bool


Algorithm:
    define a recursion_level = 0
    iterate through the string,
        when you find a '(' then recursion_level + 1
        when you find a ')' then recursion_level - 1
    if the recursion level is 0 then return True else return False

"""


def is_balanced(string:str)->bool:
    recursion = 0
    for char in string:
        if recursion < 0:
            return False
        if char == '(':
            recursion += 1
        elif char == ')':
            recursion -= 1
    return recursion == 0


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True