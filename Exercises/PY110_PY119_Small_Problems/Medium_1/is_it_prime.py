"""
a number is prime if it has no factors

"""

def is_prime(to_check:int)->bool:
    if to_check <= 1:
        return False
    ceil = int(to_check ** 0.5) + 1
    primes = []
    for n in range(2, ceil):
        not_in = True
        for num in primes:
            if n % num == 0:
                not_in = False
                break
        if not_in:
            if to_check % n == 0:
                return False
            primes.append(n)
    return True



print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
