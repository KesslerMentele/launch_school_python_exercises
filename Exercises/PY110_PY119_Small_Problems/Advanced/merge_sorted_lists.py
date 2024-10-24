"""
Input: two sorted lists
Ouput: a new list

"""



def merge(first:list, second:list)->list:
    copy_first = first.copy()
    copy_second = second.copy()
    merged_list = []
    while copy_first and copy_second:
        if copy_first[0] <= copy_second[0]:
            merged_list.append(copy_first.pop(0))
        else:
            merged_list.append(copy_second.pop(0))
    merged_list.extend(copy_first + copy_second)

    return merged_list


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)