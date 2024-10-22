import sys
sys.set_int_max_str_digits(50_000)

memo = {1: 1, 2: 1}
def fibonacci(num:int)->int:
    if num <= 2 :
        return 1
    if num in memo:
        return memo[num]
    else:
        memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return memo[num]


def find_fibonacci_index_by_length(num:int)->int:
    position = 2
    while True:
        if num == len(str(fibonacci(position))):
            return position
        position += 1
