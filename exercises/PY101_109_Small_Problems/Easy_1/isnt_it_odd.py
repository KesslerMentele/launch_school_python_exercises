# Isn't it Odd?


def is_integer_odd(number: int):
    return abs(number) % 2 != 0


print(is_integer_odd(17))   # True
print(is_integer_odd(12))   # False
print(is_integer_odd(293))  # True
print(is_integer_odd(2))    # False
print(is_integer_odd(11182))# False