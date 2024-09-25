# Floating Point Arithmetic

def get_number(message):
    response = input(message)
    try:
        return float(response)
    except ValueError:
        print('please input only the number as a whole number or decimal, no units')
        return get_number(message)

def floating_math():
    num_one = get_number('Enter the first number:')
    num_two = get_number('Enter the second number:')
    print(f'{num_one} + {num_two} = {num_one + num_two}')
    print(f'{num_one} - {num_two} = {num_one - num_two}')
    print(f'{num_one} * {num_two} = {num_one * num_two}')
    print(f'{num_one} / {num_two} = {num_one / num_two}')
    print(f'{num_one} // {num_two} = {num_one // num_two}')
    print(f'{num_one} % {num_two} = {num_one % num_two}')
    print(f'{num_one} ** {num_two} = {num_one ** num_two}')

floating_math()