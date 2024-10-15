
def select_fruit(produce_dictionary:dict)->dict:
    fruits_dict = {}
    for key, value in produce_dictionary.items():
        if value == 'Fruit':
            fruits_dict[key] = value
    return fruits_dict


def double_numbers(numbers):
    doubled_nums = []

    for current_num in numbers:
        doubled_nums.append(current_num * 2)

    return doubled_nums


def double_numbers_mutated(numbers:[int])->[int]:
    for index in range(len(numbers)):
        numbers[index] *= 2
    return numbers

def multiply_mutated(numbers:[int], multiplier:int)->[int]:
    for index in range(len(numbers)):
        numbers[index] *= multiplier
    return numbers


