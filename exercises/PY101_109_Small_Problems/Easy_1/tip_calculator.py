# Tip Calculator

def get_number(message):
    response = input(message)
    try:
        return float(response)
    except ValueError:
        print('please input only the number as a whole number or decimal, no units')
        return get_number(message)


def calculate_tip():
    bill = get_number('What is the bill?')
    tip_percent = get_number('What is the tip percentage?')
    print(f'The tip is ${(tip_percent * bill) / 100.0:.2f}')
    print(f'The tip is ${((tip_percent * bill) / 100.0) + bill:.2f}')

calculate_tip()