'''
Full Description:
Given an unordered list and the information that exactly one value in the list
occurs twice (every other value occurs exactly once), determine which value
occurs twice. Write a function that finds and returns the duplicate value.

You may assume that the input list will always have exactly one duplicate value.

Input: Unordered list
Ouput: the duplicate value, unknown type


Rules:
    Explicit:
    - the input is not ordered
    - the input has exactly one duplicate value

Algorithm:
    initialize a new list from a set from the original list
    use list comprehension to get a new list that contains only the duplicate
        - initialize a new list containing each item that exists in the
        original list and not in the duplicateless list, if it does exist in
        the duplicateless list, remove it from the duplicateless list


'''


def find_dup(original_list:[any])->any:
    pass

def find_dup_alt(original_list:[any])->any:
    duplicateless = list(set(original_list))
    only_duplicate = [item for item in original_list if not item in duplicateless or duplicateless.remove(item)]
    return only_duplicate[0]

print(find_dup_alt([1, 5, 3, 1]) == 1) # True
print(find_dup_alt([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True