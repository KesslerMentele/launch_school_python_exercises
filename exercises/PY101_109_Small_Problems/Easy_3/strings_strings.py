# Strings Strings

def stringy(length):
    result = ''
    for value in range(1,length+1):
        result = result + str(value % 2)
    return result


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True