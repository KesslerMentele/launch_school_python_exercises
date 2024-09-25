# Short Long Short

def short_long_short(string_one, string_two):
    if len(string_one) > len(string_two):
        return string_two + string_one + string_two
    else:
        return string_one + string_two + string_one

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")