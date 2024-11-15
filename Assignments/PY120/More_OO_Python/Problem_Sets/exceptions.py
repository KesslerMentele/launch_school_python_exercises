def division():
    num1 = input('Give me the first number:')
    num2 = input('Give me the second number:')
    try:
        result = int(num1) / int(num2)
    except (ZeroDivisionError, ValueError) as e:
        print(e)
    else:
        print(result)
    finally:
        print('End of the program')


class NegativeNumberError(ValueError):
    pass

def get_number():
    num = float(input("Give me a number"))
    if  num < 0:
        raise NegativeNumberError('number cannot be less than zero')



def inverse_list(numbers:list):
    if not isinstance(numbers, list):
        return 'Parameter must be a list'
    if not all([isinstance(num, int) or isinstance(num, float) for num in numbers]):
        return 'All items in the parameter list must be numbers'

    inversed = []
    for num in numbers:
        try:
            inversed.append(1/num)
        except ZeroDivisionError:
            inversed.append(float('inf'))
    return inversed

students = {'John': 25, 'Jane': 22, 'Doe': 30}
def get_age(name):
    try:
        return students[name]
    except KeyError:
        return 'Student not found'



numbers = [1, 2, 3, 4, 5]

def lbyl_sixth(items:list):
    if not isinstance(items, list):
        return None
    if len(items) <= 5:
        return None
    return items[5]

def afnp_sixth(items:list):
    try:
        return items[5]
    except IndexError:
        return None

