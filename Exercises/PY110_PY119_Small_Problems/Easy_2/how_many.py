"""
Full Description:
Write a function that counts the number of occurrences of each element in a
given list. Once counted, print each element alongside the number of
occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").


Inputs: list
Outputs: print occurrences

Rules:
    Explicit:
        - Case sensitive
    Implicit:


Algorithm:
    create an empty dict called counts
    for each item in the list
        if it is not in counts add the item to counts with a value of 1
        if it is in counts then add 1 to its value
    iterate through the dict and print '{key} => {value}'

"""

def count_occurrences(sequence:list)->None:
    counts = {}
    for item in sequence:
        if item in counts.keys():
            counts[item] += 1
        else:
            counts[item] = 1
            
    for key, value in counts.items():
        print(f'{key} => {value}')





vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)