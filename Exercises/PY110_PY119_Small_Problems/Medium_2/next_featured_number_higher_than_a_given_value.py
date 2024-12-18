"""
a featured number:
- Odd
- Multiple of 7
- with digits 0-9 occurring at most once each

Input: an integer
Output: integer equaling the next featured number larger than the given integer


"""

def next_featured(floor:int)->int | str:

    def is_valid(num:int)->bool:
        if num % 2 == 0 or num % 7 != 0:
            return False
        if len(str(num)) != len(set(str(num))):
            return False
        return True

    while True:
        if is_valid(floor + 1):
            return floor + 1
        else:
            floor += 1



print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True