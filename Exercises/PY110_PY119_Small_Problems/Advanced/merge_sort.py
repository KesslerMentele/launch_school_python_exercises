"""
Input: list of values
Output: Those values sorted

step 1: Break into nested sublists, until each bottom list contains only one element
step 2: merge the sublists, until no recusive lists
step 3: return sorted list

Algorithm:
    if the list is length one, return the list
    split the list in half, call this function on each half
    return the merged halves

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

def merge_sort(unsorted:list)->list:
    if len(unsorted) == 1:
        return unsorted
    first_half = unsorted[:len(unsorted) //2]
    second_half = unsorted[len(unsorted) //2:]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    return merge(first_half, second_half)

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)