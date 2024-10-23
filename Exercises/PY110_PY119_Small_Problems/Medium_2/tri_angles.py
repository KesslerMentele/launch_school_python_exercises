"""

input: three integer degree values
output: string of type from:
    acute
    right
    obtuse
    invalid

"""



def triangle(angle_a:int,angle_b:int,angle_c:int)->str:
    angles = sorted([angle_a,angle_b,angle_c])
    if (sum(angles) != 180
            or any(angle <= 0 for angle in angles)):
        return 'invalid'
    if angles[2] == 90:
        return 'right'
    elif angles[2] > 90:
        return 'obtuse'
    return 'acute'


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

# Additional test cases, to be sure it works
print(triangle(45, 45, 90) == "right")      # True
print(triangle(80, 50, 50) == "acute")      # True
print(triangle(100, 40, 40) == "obtuse")    # True
print(triangle(90, 45, 45) == "right")      # True
print(triangle(180, 0, 0) == "invalid")     # True
print(triangle(60, 60, 60) == "acute")      # True
print(triangle(89, 89, 2) == "acute")       # True
print(triangle(91, 44, 45) == "obtuse")     # True
print(triangle(179, 1, 0) == "invalid")     # True
