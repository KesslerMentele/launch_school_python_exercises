
def ask_age():
    age = input('How old are you? ')
    if age.isnumeric() == False:
        print('Please enter a valid number (only digits 0-9, no punctuation)')
        return ask_age()
    return int(age)


def main():
    number_age = ask_age()
    DECADES = 40
    years_passed = 10
    print(f'\nYou are {number_age} years old')
    while years_passed <= DECADES:
        print(f'In {years_passed} years, you will be {number_age + years_passed} years old.')
        years_passed += 10


if __name__ == '__main__':
    main()