# Check Prefix

def starts_with(string, check_for):
    return string.startswith(check_for)


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True