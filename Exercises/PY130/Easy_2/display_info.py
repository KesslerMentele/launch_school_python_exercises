def display_info(data, / , reverse=False, uppercase=False):
    if uppercase:
        data = data.upper()
    if reverse:
        data = data[::-1]
    return data

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC