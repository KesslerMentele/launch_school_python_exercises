"""
The issue is the if statement is trying to get the value at a key that doesn't exist, as opposed to checking if the key
exists.

To fix we use if key in my_dict.keys()
"""


def get_key_value(my_dict, key):
    if key in my_dict.keys():
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))
