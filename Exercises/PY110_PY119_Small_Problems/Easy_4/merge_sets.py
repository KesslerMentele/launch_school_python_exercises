list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]

def merge_sets(merge_one:list, merge_two:list)->set:
    return set(merge_one) | set(merge_two)


print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True