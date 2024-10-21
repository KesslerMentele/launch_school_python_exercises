"""
The issue was that the function decrease took in an argument called 'counter' which made a local variable with the same
name as the global variable. Because integers are immutable, when the local variable changed its value was reassigned to
the new value and did not affect the global value. To fix it, we simply take the return value of the decrease function
and reassign the global counter to that value.
"""


def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')


