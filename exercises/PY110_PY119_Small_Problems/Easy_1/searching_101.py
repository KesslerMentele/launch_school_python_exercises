# Searching 101

def get_number(place):
    num = input(f'Enter the {place} number:')
    try:
        return int(num)
    except ValueError:
        print('Please enter a valid number.')
        return get_number(place)


def is_in_five():
    num_1 = get_number('1st')
    num_2 = get_number('2nd')
    num_3 = get_number('3rd')
    num_4 = get_number('4th')
    num_5 = get_number('5th')
    last = get_number('last')
    num_list = [num_1, num_2, num_3, num_4, num_5]
    if last in num_list:
        return f'{last} is in {str(num_list)[1:-1]}'
    else:
        return f'{last} isn\'t in {str(num_list)[1:-1]}'

print(is_in_five())