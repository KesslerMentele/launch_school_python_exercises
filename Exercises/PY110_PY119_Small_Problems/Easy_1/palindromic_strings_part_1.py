# Palindromic Strings (Part 1)

def is_palindrome(string):
    return True if string[0::] == string[::-1] else False

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)


