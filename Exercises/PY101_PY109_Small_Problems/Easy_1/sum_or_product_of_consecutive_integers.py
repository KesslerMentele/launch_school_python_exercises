# Sum or Product of Consecutive Integers
from math import prod

def get_int_over_zero(message):
    response = input(message)
    try:
        value = int(response)
        return value if value > 0 else get_int_over_zero(message)
    except ValueError:
        print('please input only a number as a whole number greater than zero, no units')
        return get_int_over_zero(message)

def get_input_string():
    response = input('Enter "s" to compute the sum, or "p" to compute the product.')
    if response == 's' or response == 'p':
        return response
    else:
        return get_input_string()


def sum_or_product():
    value = get_int_over_zero('Please enter an integer greater than 0:')
    operation = get_input_string()
    print(operation)
    match operation:
        case 's':
            print(f'The sum of the integers between 1 and {value} is '
                  f'{sum(range(1, (value + 1)))}')
            return
        case 'p':
            print(f'The sum of the integers between 1 and {value} is '
                  f'{prod(range(1, (value + 1)))}')


sum_or_product()