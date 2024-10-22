"""
The code provided changes the size of the set as it iterates. To prevent this
we can use a set comprehension instead.
"""


data_set = {1, 2, 3, 4, 5}

data_set = {item for item in data_set if item % 2 != 0}
