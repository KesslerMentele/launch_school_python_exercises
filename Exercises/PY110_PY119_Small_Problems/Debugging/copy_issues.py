"""
The copy() function performs a shallow copy, meaning that the objects
referenced in the copied list are the same ones as the original list. To fix
this we need to perform a deep copy on the list, so that the objects in the
list are also copied
"""


import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])