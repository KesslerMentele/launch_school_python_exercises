

def leading_substrings(orig:str)->list:
    return [orig[:idx + 1] for idx in range(len(orig))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])