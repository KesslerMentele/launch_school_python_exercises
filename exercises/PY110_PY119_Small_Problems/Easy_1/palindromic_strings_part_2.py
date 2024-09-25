# Palindromic Strings (Part 2)


def is_real_palindrome(string):
    stripped_string = ''
    for char in string:
        stripped_string += char.lower() if char.isalnum() else ''
    return True if stripped_string[0::] == stripped_string[::-1] else False


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True