

def keep_keys(dict_in:dict, keys_to_keep:list)->dict:
    return {key:val for key, val in dict_in.items() if key in keys_to_keep}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True