

def multiply_items(list_one:list, list_two:list)->list:
    return [item[0] * item[1] for item in zip(list_one, list_two)]


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True