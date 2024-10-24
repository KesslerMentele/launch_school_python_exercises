"""
Input: list
Output: None, a mutation of the list


"""

def bubble_sort(input_list:list)->None:
    is_sorted = False

    while not is_sorted:
        did_sort = False
        for index in range(len(input_list) - 1):
            if input_list[index] > input_list[index + 1]:
                did_sort = True
                input_list[index] , input_list[index + 1] = input_list[index + 1],  input_list[index]

        is_sorted = not did_sort


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True