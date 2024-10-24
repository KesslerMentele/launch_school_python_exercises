"""

the default list is the same list across function calls, so mutating it mutates it for all future calls

"""


def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
