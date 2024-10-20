

def intersection(merge_one, merge_two)->frozenset:
    return frozenset(merge_one).intersection(set(merge_two))


list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True