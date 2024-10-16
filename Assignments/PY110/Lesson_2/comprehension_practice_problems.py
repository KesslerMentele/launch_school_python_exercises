

# Practice Problem 1
def problem_one():
    munsters = {
        'Herman': {'age': 32, 'gender': 'male'},
        'Lily': {'age': 30, 'gender': 'female'},
        'Grandpa': {'age': 402, 'gender': 'male'},
        'Eddie': {'age': 10, 'gender': 'male'},
        'Marilyn': {'age': 23, 'gender': 'female'},
    }

    #Loop
    ages = 0
    for munster in munsters.values():
        if munster['gender'] == 'male':
           ages += munster['age']
    print(ages)

    #Comprehension
    print(sum([info['age'] for info in munsters.values()
               if info['gender'] == 'male' ]))


# Practice Problem 2
def problem_two():
    lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
    new_lst = [sorted(sublist) for sublist in lst]
    print(new_lst)


# Practice Problem 3
def problem_three():
    lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
    new_lst = [sorted(sublist, key=str) for sublist in lst]
    print(new_lst)


# Practice Problem 4
def problem_four():
    lst = [
        ['a', 1],
        ['b', 'two'],
        ['sea', {'c': 3}],
        ['D', ['a', 'b', 'c']]
    ]

    as_dictionary = {key:value for key,value in lst}
    print(as_dictionary)


# Practice Problem 5
def problem_five():
    lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
    def sum_odds(numbers):
        return sum([number for number in numbers if number % 2 != 0])
    oddly_sorted = sorted(lst, key=sum_odds)
    print(oddly_sorted)
    print(f'original:{lst}')


# Practice Problem 6
def problem_six():
    lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

    added_lst = [{key:value + 1
                  for key, value in value.items()}
                 for value in lst]
    print(added_lst)


# Practice Problem 7
def problem_seven():
    lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
    triples_lst = [[item for item in sublist
                    if item % 3 == 0]
                   for sublist in lst]
    print(triples_lst)


# Practice Problem 8
def problem_eight():
    dict1 = {
        'grape': {
            'type': 'fruit',
            'colors': ['red', 'green'],
            'size': 'small',
        },
        'carrot': {
            'type': 'vegetable',
            'colors': ['orange'],
            'size': 'medium',
        },
        'apricot': {
            'type': 'fruit',
            'colors': ['orange'],
            'size': 'medium',
        },
        'marrow': {
            'type': 'vegetable',
            'colors': ['green'],
            'size': 'large',
        },
    }

    def veggie_or_fruit(dictionary:dict):
        return dictionary['size'].upper() if dictionary['type'] == 'vegetable' \
            else [item.capitalize() for item in dictionary['colors']]


    info = [veggie_or_fruit(produce) for produce in dict1.values()]
    print(info)


# Practice Problem 9
#
# Input: list of dictionaries with values of lists of numbers
# Output: list of dictionaries with values of lists of only even numbers

def problem_nine():
    lst = [
        {'a': [1, 2, 3]},
        {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
        {'e': [8], 'f': [6, 10]},
    ]

    def all_numbers_even(dictionary:dict)->bool:
        return all([ True if item % 2 == 0 else False
                     for value in dictionary.values()
                     for item in value ])

    new_lst = [dictionary for dictionary in lst
               if all_numbers_even(dictionary)]

    print(new_lst)


# Practice Problem ten
def problem_ten():
    import random
    def hexc(length):
        hex = '0123456789abcdef'
        return ''.join([hex[random.randint(0,15)]
                         for _ in range(length)])

    print(f'{hexc(8)}-{hexc(4)}-{hexc(4)}-{hexc(4)}-{hexc(12)}')


# Practice Problem eleven
def problem_eleven():
    dict1 = {
        'first': ['the', 'quick'],
        'second': ['brown', 'fox'],
        'third': ['jumped'],
        'fourth': ['over', 'the', 'lazy', 'dog'],
    }
    list_of_vowels = []
    for dictionary in dict1.values():
        for item in dictionary:
            for char in item:
                if char in 'aeiou':
                    list_of_vowels.append(char)

    one_shot_list = [char for dictionary in dict1.values()
                     for item in dictionary
                     for char in item
                     if char in 'aeiou']

    print(list_of_vowels)
    print(one_shot_list)
    # ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
