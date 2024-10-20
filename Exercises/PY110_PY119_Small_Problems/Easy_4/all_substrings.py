
def substrings(orig:str)->list:
    return [orig[start:end+1] for start in range(len(orig)) for end in range(len(orig)) if end >= start]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True