

def multiply(numbers):
    equation_value = 1
    result = ''
    for i in range(len(numbers)):
        equation_value *= numbers[i]

        if i == len(numbers) - 1:
            result += f"{numbers[i]} = {equation_value}"
        else:
            result += f"{numbers[i]} * "

    return result


def ask_for_numbers(count):
    numbers = []
    for i in range(count):
        number = input(f"Enter the {i + 1}{get_ordinal(i + 1)} number: ")
        if number.isnumeric():
            number = int(number)
            numbers.append(number)
        else:
            print("Please enter valid numbers.")
            return ask_for_numbers(count)
    return numbers


def get_ordinal(number):
    last_digit = number  % 10
    if last_digit == 1:
        return 'st'
    elif last_digit == 2:
        return 'nd'
    elif last_digit == 3:
        return 'rd'
    else:
        return 'th'


def main():
    NUMBERS_COUNT = 2
    numbers = ask_for_numbers(NUMBERS_COUNT)
    result = multiply(numbers)
    print(f"The result is {result}")


if __name__ == "__main__":
    main()