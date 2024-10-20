

def unique_from_first(orig_list:list, filter_list:list)->set:
    return {item for item in orig_list if item not in filter_list}


list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})