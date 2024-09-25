# Convert a Number to a String

def digit_converter(number:int):
    match number % 10:
        case 1:
            return '1'
        case 2:
            return '2'
        case 3:
            return '3'
        case 4:
            return '4'
        case 5:
            return '5'
        case 6:
            return '6'
        case 7:
            return '7'
        case 8:
            return '8'
        case 9:
            return '9'
        case 0:
            return '0'


def integer_to_string(number:int):
    final_string = ''
    if number == 0:
        return '0'
    while number != 0:
        split = divmod(number, 10)
        final_string = final_string + digit_converter(split[1])
        number = split[0]
    return final_string[::-1]


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True