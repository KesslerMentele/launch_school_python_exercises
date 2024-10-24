"""

Algorithm:
    get middle value
    if middle == target: return index of item
    else if middle < target
        rerun on list from middle to end as half_index
        return half length + half_index
    else if middle > target
        rerun on list from beginning to middle as half_index
        return half_index
    else return -1

"""


def binary_search(items:list, target:any)->int:
    if len(items) == 1 and items[0] != target:
        return -1
    middle = len(items) // 2
    if items[middle] == target:
        return middle
    elif items[middle] < target:
        half_index = binary_search(items[middle:], target)
        if half_index < 0:
            return -1
        return middle + half_index
    elif items[middle] > target:
        half_index =  binary_search(items[:middle], target)
        if half_index < 0:
            return -1
        return half_index

businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)