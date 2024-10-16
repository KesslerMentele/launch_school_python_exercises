'''
Full Description:
Write a function that combines two lists passed as arguments and returns a new
list that contains all elements from both list arguments, with each element
taken in alternation.

You may assume that both input lists are non-empty, and that they have the same
number of elements.

Input: two lists
Output: one list, with alternating elements

Rules:
    Output list must contain all elements of both input lists
    The input lists are not empty

Algorithm:
    zip the two lists together
    for each pair, for each item add it to the returned list using list comprehension
'''


def interleave(first_list:list,second_list:list)->list:
    return [item for pair in zip(first_list, second_list) for item in pair]




list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True