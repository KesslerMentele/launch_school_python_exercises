"""
Full Description:
Write a function that takes a list as an argument and reverses its elements,
in place. That is, mutate the list passed into the function. The returned
object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).

Input: list
Output: the same list, reversed

Rules:
    Explicit:
        No reverse()
        No slicing

Algorithm:
    create length = len(input_list)
    for index in range(length):
        item = input_list.pop()
        input_list.push(index, item)
    return input_list


"""

def reverse_list(input_list):
    length = len(input_list)
    for index in range(length):
        item = input_list.pop()
        input_list.insert(index, item)
    return input_list

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True