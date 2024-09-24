# Exclusive Or

def xor(arg_1, arg_2):
    return False if arg_1 and arg_2 else True if arg_1 or arg_2 else False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)