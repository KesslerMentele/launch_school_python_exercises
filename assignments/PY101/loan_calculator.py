# Mortgage / Car Loan Calculator

# Known Issues:
#
# - Very Small APR values that round to zero cause division-by-zero error.
#
# - Recursive input handling can lead to hitting maximum recursion depth after
#   around 999 consecutive failed inputs.

import json

with open('loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def get_input(message, value_type = str):
    value = input(message)
    if isinstance(value, value_type):
        return value
    value = convert_to_type(value, value_type)
    if value <= 0:
        print(MESSAGES['non_positive_value'])
        return get_input(message, value_type)
    if not value:
        print(MESSAGES['invalid_type']
              .format(name = value_type.__name__))
        return get_input(message, value_type)
    return value


def convert_to_type(value, new_type):
    try:
        return new_type(value)
    except ValueError:
        return None


def get_interest_rate():
    user_value = get_input(MESSAGES['apr'])
    is_percent = False
    if '%' in user_value:
        user_value = user_value.replace('%', '')
        is_percent = True

    final_value = convert_to_type(user_value, float)
    if not final_value and final_value != 0:
        print(MESSAGES['invalid_apr'])
        return get_interest_rate()
    return final_value if not is_percent else final_value / 100


def get_loan_amount():
    user_value = get_input(MESSAGES['loan'])
    user_value = user_value.replace('$', '')
    user_value = user_value.replace(',', '')
    final_value = convert_to_type(user_value, float)
    if not final_value:
        print(MESSAGES['invalid_loan'])
        return get_loan_amount()
    return final_value

def get_loan_duration():
    duration = get_input(MESSAGES['duration'], int)
    duration_type = get_input(MESSAGES['duration_type'])
    duration_type = duration_type.casefold()
    match duration_type:
        case 'm':
            return duration
        case 'y':
            return duration * 12
        case _:
            print(MESSAGES['invalid_duration_type'])
            return get_loan_duration()

def loan_calculator():
    loan = get_loan_amount()
    interest_rate = get_interest_rate()
    monthly_rate = interest_rate / 12

    duration_months = get_loan_duration()
    if monthly_rate:
        monthly_payment = (loan * (monthly_rate / (1 - (1 + monthly_rate)**
                                                   (-duration_months))))
    else:
        monthly_payment = loan / duration_months

    print(MESSAGES['result_value']
          .format(payment = round(monthly_payment,2)))
    print(MESSAGES['result_duration']
          .format(duration_months = duration_months))

loan_calculator()