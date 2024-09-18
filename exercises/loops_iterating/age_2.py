
def ask_age():
    age = input('How old are you? ')
    if age.isnumeric() == False:
        print('Please enter a valid number (only digits 0-9, no punctuation)')
        return ask_age()
    return int(age)


def main():
    number_age = ask_age()
    decades = range(10, 50, 10)

    print(f'\nYou are {number_age} years old')
    for decade in decades:
        print(f'In {decade} years, you will be {number_age + decade} years old.')


if __name__ == '__main__':
    main()