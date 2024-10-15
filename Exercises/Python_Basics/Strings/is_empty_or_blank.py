# Is Empty or Blank?

def is_empty_or_blank(string_input):
    return len(string_input) == 0 or string_input.isspace()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True