'''
Full Description:
Write a function that takes a list as an argument and returns a list that
contains two elements, both of which are lists. Put the first half of the
original list elements in the first element of the return value and put the
second half in the second element. If the original list contains an odd number
of elements, place the middle element in the first half list.


Input: List
Output: List of two halves lists of original list

What if the original list is empty?

Rules:
    Explicit:
    - If the list is not even, the first return sublist should have the extra

Algorithm:
    create a new list called halves
    create a new list called first_half
    create a new list called second_half
    for each item in the original_list
        if the index < (len(original_list) / 2)
            append to first_half
        else append to second_half
    add both lists to the halves list and return it

'''


def halvsies(original:[])->[[]]:
    halves = []
    first_half = []
    second_half = []
    size = len(original)
    for index in range(size):
        if index < (size / 2 ):
            first_half.append(original[index])
        else:
            second_half.append(original[index])
    halves.append(first_half)
    halves.append(second_half)
    return halves

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])