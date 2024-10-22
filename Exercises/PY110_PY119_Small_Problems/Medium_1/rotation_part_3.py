"""
Full Problem:
Take the number 735291 and rotate it by one digit to the left, getting 352917.
Next, keep the first digit fixed in place and rotate the remaining digits to
get 329175. Keep the first two digits fixed in place and rotate again to get
321759. Keep the first three digits fixed in place and rotate again to get
321597. Finally, keep the first four digits fixed in place and rotate the final
two digits to get 321579. The resulting number is called the maximum rotation
of the original number.

so the process described is:

- Take Input number                                 735291
- Rotate it once to the left
    -                                               7<-35291
    -                                               35291<-7
    -                                               352917
- now lock the first digit in place                [3] 52917
- rotate the remaining digits once to the left     [3] 29175
- lock the second digit and do the rotation again  [32] 1759
- lock the third digit and do the rotation again   [321] 597
- lock the fourth digit and do the rotation again  [3215] 79
- return that number                                321579


"""

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

def max_rotation(input_num:int)->int:
    digits = list(str(input_num))
    for count in range(len(digits), 1, -1):
        input_num = rotate_rightmost_digits(input_num, count)
    return input_num

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True


'''
8703529146

7


'''
