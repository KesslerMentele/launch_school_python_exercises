

def unique_sequence(in_list:list)->list:
    prev_val = None
    result = []
    for item in in_list:
        if item != prev_val:
            result.append(item)
        prev_val = item
    return result


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True