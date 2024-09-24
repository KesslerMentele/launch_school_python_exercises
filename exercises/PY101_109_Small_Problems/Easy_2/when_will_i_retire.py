# When Will I Retire?

from datetime import datetime

def get_number(message):
    response = input(message)
    try:
        return int(response)
    except ValueError:
        print('please input only the number as a whole number')
        return get_number(message)

def when_will_i_retire():
    age = get_number('What is your age?')
    retirement_age = get_number('At what age would you like to retire?')
    year = datetime.now().year
    print(f'It\'s {year}. You will retire in {year + (retirement_age - age)}')
    print(f'You have only {retirement_age - age} years of work to go!')


when_will_i_retire()