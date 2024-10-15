

def count_max_adjacent_consonants(string:str)-> int:
    index = 0
    total = 0
    count = 0
    while index < len(string):
        if is_consonant(string[index]):
            count += 1
        total = count if count > total else total
        if is_vowel(string[index]):
            count = 0
        index += 1

    return total if total > 1 else 0


def is_consonant(char: str) -> bool:
    if not is_vowel(char) and char.isalpha():
        return True
    return False


def is_vowel(char: str) -> bool:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True


def sort_by_consonant_count(unsorted_list):
    unsorted_list.sort(reverse=True, key=count_max_adjacent_consonants)
    return unsorted_list


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']