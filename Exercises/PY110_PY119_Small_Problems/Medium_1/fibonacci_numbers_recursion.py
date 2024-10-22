"""
Recursive Fibonacci

using the identities:

F(2 * k) = F(k) * (2 * F(k + 1) - F(k))

and

F(2 * k + 1) = F(K)**2 + F(K + 1)**2

we can create a recursive function that instead of stepping through every value
in the sequence, it uses doubling formulas to only have to step through a
number of times equal to or less than the log base 2 of n.

This means a traditional fibonacci algorithm with n = 1000 would have a depth
of 1000, while this method would have a depth of 9.


"""
import sys

sys.set_int_max_str_digits(0)

def fibonacci(num:int)->int:
    return recursive_fib(num)[0]

def recursive_fib(num:int)->tuple:
    if num == 0:
        return 0,1
    else:
        a, b = recursive_fib(num //2)
        c = a * ((b * 2) - a)
        d = (a * a) + (b * b)
        if num % 2 == 0:
            return c, d
        else:
            return d, c + d


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True