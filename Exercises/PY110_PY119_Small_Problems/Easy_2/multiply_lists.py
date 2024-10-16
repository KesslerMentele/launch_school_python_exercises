"""
Full Description:
Write a function that takes two list arguments, each containing a list of
numbers, and returns a new list that contains the product of each pair of
numbers from the arguments that have the same index. You may assume that the
arguments contain the same number of elements.

Input: Two lists
Output: one list

rules:
    Explicit:
        - Both lists have the same number of elements
        - Lists contain only numbers

Algorithm:
    Zip together both lists
    use list comprehension to multiply each tuple and return it to a new list


"""


def multiply_list(first_list:list,second_list:list)->list:
    return [multiplicand * multiplier for multiplicand, multiplier in zip(first_list, second_list)]


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True