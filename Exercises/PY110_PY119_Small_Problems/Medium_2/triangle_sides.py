

def triangle(side_a: int | float, side_b: int | float, side_c: int | float)->str:

    sized = sorted([side_a, side_b, side_c])

    if side_a <= 0 or side_b <= 0 or side_c <= 0 or sum(sized[:2]) < sized[2]:
        return 'invalid'

    if side_a == side_b == side_c:
        return 'equilateral'

    if side_a == side_b or side_a == side_c or side_c == side_b:
        return 'isosceles'

    return 'scalene'



print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True