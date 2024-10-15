# Get Middle Character

def center_of(string):
    middle = len(string) // 2
    if len(string) % 2 == 0:
        return string[middle-1: middle + 1]
    else:
        return string[middle:middle+1]


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True