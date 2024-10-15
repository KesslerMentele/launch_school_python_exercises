# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.
import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def message(message, lang="en"):
    return MESSAGES[lang][message]

def calculator():

    print(message("welcome"))

    number_1 = prompt(message("first"))

    while invalid_number(number_1):
        number_1 = prompt(message('invalid_number'))

    number_1 = float(number_1)

    number_2 = prompt(message("second"))

    while invalid_number(number_2):
        number_2 =  prompt(message('invalid_number'))

    number_2 = float(number_2)

    operator_number = prompt(message('operator'))

    while operator_number not in ['1', '2', '3', '4']:
        operator_number = prompt(message('invalid_operator'))

    match operator_number:
        case '1':
            output = number_1 + number_2
        case '2':
            output = number_1 - number_2
        case '3':
            output = number_1 * number_2
        case '4':
            output = number_1 / number_2
        case _:
            output = "not defined"

    print(message('result').format(output=output))
    again = prompt(message('again'))
    while again != 'Y' and again != 'N':
        print (again)
        again = prompt('')
    return calculator() if again == 'Y' else None

def prompt(text):
    return input(f'==> {text}\n')

def invalid_number(number_string):
    try:
        float(number_string)
    except ValueError:
        return True
    return False

calculator()