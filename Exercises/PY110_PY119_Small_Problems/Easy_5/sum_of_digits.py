



def sum_digits(num:int)->int:
    return sum([int(char) for char in str(num)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True