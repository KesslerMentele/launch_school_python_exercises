

def remove_vowels(orig:list)->list:
    vowels = 'aeiou'


    def cut_out(string_in:str, to_filter:str)->str:
        return ''.join([char for char in string_in if char.lower() not in to_filter])


    return [cut_out(string, vowels) for string in orig]


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True