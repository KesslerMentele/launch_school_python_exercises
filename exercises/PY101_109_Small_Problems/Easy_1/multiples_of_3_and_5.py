# Multiples of 3 and 5


def multisum(number):
    total = 0
    for step in range(1,number+1):
        total += step if step % 3 == 0 or step % 5 == 0 else 0
    return total

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)