# Travel

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']


def contains(search_for, list_to_check):
    if not isinstance(list_to_check, list):
        return None
    for item in list_to_check:
        if item == search_for:
            return True

    return False


print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
