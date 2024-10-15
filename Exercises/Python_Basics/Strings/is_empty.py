# Is Empty?

def is_empty(string_input):
    return len(string_input) == 0

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True