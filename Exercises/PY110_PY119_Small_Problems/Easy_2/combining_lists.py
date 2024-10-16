'''
Full Description:
Write a function that takes two lists as arguments and returns a set that
contains the union of the values from the two lists. You may assume that both
arguments will always be lists.


Input: Two Lists
Output: A Set

What if the lists are empty?

rules:
    Explicit:
    - Union two lists into a set
    Implicit:

Algorithm:
    return set(a+b)
'''


def union(list_one:[],list_two:[])-> set:
    return set(list_one + list_two)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True