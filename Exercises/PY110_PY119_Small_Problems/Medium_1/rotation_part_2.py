

def rotate_list(input_list:list)->list | None:
    if not isinstance(input_list, list):
        return None
    new_list = []
    if len(input_list) == 0:
        return new_list

    new_list.extend(input_list[1:])
    new_list.append(input_list[0])
    return new_list


def rotate_rightmost_digits(input_num:int, count:int)->int:
    digits = list(str(input_num))
    return int(''.join(digits[:-count] + rotate_list(digits[-count:])))


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True