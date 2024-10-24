"""
Input: integer
Output: integer


"""



def sum_square_difference(num_to:int)->int:
    values = {}
    for count in range(1, num_to + 1):
        values[count] = count**2
    return sum(values.keys())**2 - sum(values.values())


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True